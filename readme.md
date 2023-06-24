# 👿PDF 파싱 & 감염 PDF 탐지👿
<br>

<h2>Ⅰ. 프로젝트 소개 </h2>
<h3> <개요> </h3>
 • PDF를 파싱하여 구조를 분석하고, 감염 여부를 판단하는 웹 서비스<br>
<br>

<h3> <배경> </h3>
 • 매우 빈번히 사용되는 문서 형식인 PDF에 악의적인 코드가 심어졌을때 큰 피해가 발생할 수 있음을 인지<br>
<br>


<h2>Ⅱ. 프로젝트 목표 </h2>
 • 각종 정상 PDF와 감염 PDF를 파싱하여 구조를 분석<br>
 • 머신 러닝 모델에 해당 PDF들의 특성을 학습시키고, 감염 여부를 판별하는 서비스를 제공<br>
<br>

<h2>Ⅲ. 주요 화면 및 시연 영상 </h2>
<h3>1. 메인 화면 </h3>
_/upload_ <br>

![image](https://user-images.githubusercontent.com/79822913/147897628-d1b3e6fb-0504-4043-9b96-a7a41ccf2bb0.png)<br>
해당 화면에서 감염 여부를 판별하고자 하는 PDF를 하나 이상 업로드<br>

<h3>2. 결과 화면</h3>
_/uploader_<br>

![image](https://user-images.githubusercontent.com/79822913/147897642-3e23a61b-fb2e-494f-954d-501b1624f4cf.png)<br>
업로드된 PDF의 감염 여부를 출력<br>

<h3>3. 시연 영상</h3>

https://user-images.githubusercontent.com/79822913/173197709-1891cb5c-8194-4e81-b0a0-08746a96932a.mp4

<br>
<br>


## ✏️ How to use 
### 1. Cloning
```
$ git clone https://github.com/harloxx/Web-security.git
```
### 2. Make Virtual Environment & Download Requirements
+ Project Environment : VMware Workstation 16 Player, Ubuntu 16.04
+ Go to *Web-security/* directory
```
cd Web-security
```
+ Make virtual environment
```
$ pip install virtualenv
$ virtualenv myenv # make virtual environment
```
+ Activate virtual environment
```
$ source myenv/bin/activate
```
+ Go back to Web-security directory and install requirements.txt
```
(myenv) $ pip install -r requirements.txt 
```
+ If you want to deactivate
```
(myenv) $ deactivate
```
### 3. RUN
+ Run Flask
```
(myenv) $ flask run
```


## 🔧 Directory Structure
```
├── Web-Security/                           - 백엔드 플라스크 디렉토리
    ├── package.lock.json                   - 라이브러리 관리 파일
    ├── requirements.txt                    - 모듈들을 정리한 파일
    ├── app.py                              - Flask 실행 위한 파일
    ├── output/                             - pdf의 결과가 저장되는 디렉토리
    └── templates/
         ├── upload.html                   -클라이언트로부터 pdf를 받아옴
         ├── result.html                   -클라이언트에게 pdf parsing 결과를 보여줌
         └── uploads/                      -클라이언트로 받아온 pdf를 저장하는 곳
```
## 💻 API
#### main page, pdf upload
```
GET /upload
```
#### pdf upload & pdf parsing result
```
POST /uploader
```
+ Request
```
{
    "files" : "file[]",
    "enctype" : "multipart/form-data"
}
```
+ Response
```
{
    "benign": [benign file list],
    "malicious" : [malicious file list]
}

```
