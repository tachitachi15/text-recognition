import boto3

client = boto3.client('rekognition','ap-northeast-1')

img_file_path = 'Eng.png'
img = open(img_file_path, 'rb')
img_byte = img.read()

# rekognitionのdetect_labelsに画像バイト列を渡してラベル検出
response = client.detect_text(
    Image={
        'Bytes': img_byte
    }
)

textdetections = response['TextDetections']

file = "detected sentences.txt"
fileobj = open(file,"w",encoding="utf-8")

# 返ってきたresponseから文字情報取得
# 単語ごと読み取っていく
for value in textdetections:
    if value['Type']=='WORD':
        fileobj.write(value['DetectedText'])
        fileobj.write(' ')
