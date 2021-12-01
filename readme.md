## ✏️ How to use 
### 1. Cloning
```
$ git clone https://github.com/Dayflt/Backend.git
```
### 2. Make Virtual Environment & Download Requirements
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
$ .\myenv\Scripts\activate
```
+ Go back to Web-security directory and install requirements.txt
```
(myenv) $ cd ../../
(myenv) $ pip install -r requirements.txt 
```
+ If you want to deactivate
```
(myenv) $ deactivate
```

## 🔧 Directory Structure
```
├── Web-Security/                           - 백엔드 플라스크 디렉토리
    ├── app.py                              - 모듈들을 정리한 파일
    └── templates/
         ├── malicious.html                            - AI모델 알고리즘
         ├── success.html                  - 백엔드 동영상 임시 저장 디렉토리
         ├── upload.html                           - database ORM 정의 파일
         └── uploads/

```
