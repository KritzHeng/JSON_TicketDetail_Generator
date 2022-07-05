import json

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './JSON/' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
# start with 1 to (n-1)
n = int(input("enter amount Ticket do you want to create: "))
for i in range(1,(n+1)):
    a = i
    data = {}
    data['name'] = "#%d"%(a)
    data["description"] = ""
    data["image"] = ""
    data["additional_image"] = ""

    data["attributes"] = []
    writeToJSONFile('./','%d'%(a),data)
# './' represents the current directory so the directory save-file.py is in
# 'test' is my file name