# spartamarket_DRF

스파르타 코딩 클럽 Django 심화 주간 개인 과제

## 프로젝트 소개

DRF를 사용하여 스파르타 마켓의 기본적인 기능을 백엔드로 구현하는 것

## 개발 기간

- 2024.04.26(금) ~ 2024.05.02(목)

## 개발 환경

- OS: Window, Ubuntu(WSL)
- IDE: VSCode
- Language: Python
- Github

## Requirements

- asgiref==3.8.1
- backports.zoneinfo==0.2.1
- Django==4.2.11
- django-dotenv==1.4.2
- djangorestframework==3.15.1
- sqlparse==0.5.0
- typing_extensions==4.11.0

## 기능

1. 필수 기능
   - 회원 가입
   - 로그인
   - 프로필 조회
   - 상품 등록
   - 상품 목록 조회
   - 상품 수정
   - 상품 삭제

2. 선택 기능
   - 로그아웃
   - 본인 정보 수정
   - 상품 목록 조회 페이지네이션

## ERD
![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_ERD.png)

## 실행화면
1. 회원 가입
   - 정상 작동
     ![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_signup.png)
     
   - 중복 확인
     ![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_signup_duplication.png)

-----
2. 로그인
   
   ![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_login.png)

-----
3. 로그아웃
   - 조건: 로그인 상태(Token 필요), body에 refresh Token을 넣어야 함
   - 정상 작동
     ![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_logout.png)
     
   - blacklist 확인
     ![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_blacklist.png)

-----
4. 프로필 조회
   
   - 조건: 로그인 상태(Token 필요)
   ![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_profile.png)

-----
5. 프로필 수정
   - 조건: 로그인 상태(Token 필요)
   - 정상 작동
     ![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_profileupdate.png)
     
   - 본인만 수정 가능
     ![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_profileupdate_permission.png)
     
   - 이메일 중복 확인
     ![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_profileupdate_email_validate.png)

-----
6. 상품 등록
   - 조건: 로그인 상태(Token 필요)
    ![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_productcreate.png)

-----
7. 상품 목록 조회
    - 페이지네이션 사용
    ![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_productlist.png)

-----
8. 상품 상세 조회
   ![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_productdetail.png)

-----
9. 상품 수정
    - 조건: 로그인 상태(Token 필요)
    - 정상 작동
      ![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_productupdate.png)
      
    - 작성자만 수정 가능
      ![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_productupdate_permission.png)
      
-----
10. 상품 삭제
    - 조건: 로그인 상태(Token 필요)
    ![](https://github.com/Juunsik/spartamarket_DRF/blob/main/DRF_image/DRF_productdelete.png)
