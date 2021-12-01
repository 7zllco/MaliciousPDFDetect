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
    ├── requirements.txt                    - 모듈들을 정리한 파일
    ├── app.py                              - Flask 실행 위한 파일
    └── templates/
         ├── malicious.html                -입력된 파일이 악성코드가 포함된 파일일 경우
         ├── success.html                  - 입력된 파일이 정상 파일일 경우
         ├── upload.html                   -클라이언트로부터 pdf를 받아옴
         └── uploads/                      -클라이언트로 받아온 pdf를 저장하는 곳

```
