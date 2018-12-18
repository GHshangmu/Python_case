from aip import AipFace
import base64
import cv2
# 定义常量
APP_ID = 'XXXXXXX'
API_KEY = 'XXXXXXX'
SECRET_KEY = 'XXXXXXX'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)
IMAGE_TYPE='BASE64'
id=[]
id.append(0)#23333333

f1 = open('D:\\ID1.jpg','rb')
id.append(base64.b64encode(f1.read()))
f1.close

f2 = open('D:\\ID2.jpg','rb')
id.append(base64.b64encode(f2.read()))
f2.close

f3 = open('D:\\ID3.jpg','rb')
id.append(base64.b64encode(f3.read()))
f3.close

f4 = open('D:\\ID4.jpg','rb')
id.append(base64.b64encode(f4.read()))
f4.close

f5 = open('D:\\ID5.jpg','rb')
id.append(base64.b64encode(f5.read()))
f5.close

f6 = open('D:\\ID6.jpg','rb')
id.append(base64.b64encode(f6.read()))
f6.close

def match(img):
    score=[]
    for i in range(1,7):
        params1 = [{"image":str(img,'utf-8'),"image_type":IMAGE_TYPE},{"image":str(id[i],'utf-8'),"image_type":IMAGE_TYPE}]
        result = client.match(params1);
        #print(result)
        if result['error_msg']=='pic not has face':
            print('no match ')
            return 0
        #print('match result')
        #print (result)
        tmp=result['result']['score']/100.0
        score.append(tmp)

        #print(result['result']['score'])
    #print('match result')
    print ([float("%.2f" % max(score)),score.index(max(score))+1])
    return[float("%.2f" % max(score)),score.index(max(score))+1]#最高分数和ID

def detect(img64,j):
    options = {'max_face_num': 5, }# 图像数量
    result1=client.detect(img64, "BASE64", options)
    if result1['error_msg']=='pic not has face':
        print('no face')
        return []
    faceNum=result1['result']['face_num']
    if faceNum == 0:
        return []

    img=cv2.imread('D:\\test\\{}.jpg'.format(j))
    result=[]

    for i in range(faceNum):#保存小图
        '''if result1['result']['face_list'][i]['face_probability'] >0.3:
            location=result1['result']['face_list'][i]['location']
            left_top=(int(location['left']),int(location['top']))
            right_bottom=(left_top[0]+int(location['width']),left_top[1]+int(location['height']))

            result.append([left_top,right_bottom])
            #print(left_top[1],right_bottom[1],left_top[0],right_bottom[0])
            cropImg=img[max(0,left_top[1]):max(0,right_bottom[1]),max(0,left_top[0]):max(0,right_bottom[0])]
            cv2.imwrite('D:\\cropImg\\{}.{}.jpg'.format(j,i),cropImg)'''
        location=result1['result']['face_list'][i]['location']
        left_top=(int(location['left']),int(location['top']))
        right_bottom=(left_top[0]+int(location['width']),left_top[1]+int(location['height']))

        result.append([left_top,right_bottom])
        #print(left_top[1],right_bottom[1],left_top[0],right_bottom[0])
        cropImg=img[max(0,left_top[1]):max(0,right_bottom[1]),max(0,left_top[0]):max(0,right_bottom[0])]
        cv2.imwrite('D:\\cropImg\\{}.{}.jpg'.format(j,i),cropImg)
    #print('detect result\n')
    #print(result)
    return result



if __name__ == '__main__':
    for j in range(1,101):
        print('.........................')
        print(j)
        f = open('D:\\test\\{}.jpg'.format(j),'rb')
        image = base64.b64encode(f.read())
        img64 = str(image,'utf-8')
        result_detect=detect(img64,j)
        print (len(result_detect))
        im=cv2.imread('D:\\test\\{}.jpg'.format(j))
        if result_detect==0 or result_detect==[]:
            cv2.imwrite('D:\\result\\{}.jpg'.format(j),im)
            continue

        if len(result_detect)==1:
            result_match=match(image)
            left_top,right_bottom=result_detect[0]
            cv2.rectangle(im,left_top,right_bottom,(0,0,255),2)
            text = 'ID{}'.format(result_match[1])+':{}'.format(result_match[0])
            cv2.putText(im, text, (left_top[0],left_top[1]-6), cv2.FONT_HERSHEY_SIMPLEX,3, (0, 255, 0),5 )
            cv2.imwrite('D:\\result\\{}.jpg'.format(j),im)

        if len(result_detect)>1:
            for i in range(len(result_detect)):
                f1 = open('D:\\cropImg\\{}.{}.jpg'.format(j,i),'rb')
                image = base64.b64encode(f1.read())
                result_match=match(image)
                if result_match==0:
                    cv2.imwrite('D:\\result\\{}.jpg'.format(j),im)
                    continue
                left_top,right_bottom=result_detect[i]
                cv2.rectangle(im,left_top,right_bottom,(0,0,255),2)
                text = 'ID{}'.format(result_match[1])+':{}'.format(result_match[0])
                cv2.putText(im, text, (left_top[0],left_top[1]-6), cv2.FONT_HERSHEY_SIMPLEX,3, (0, 255, 0),5 )
            cv2.imwrite('D:\\result\\{}.jpg'.format(j),im)
