import re

"""
이메일인지 검증하는 함수를 만들어주세요. 정규표현식을 사용해 주세요.
이메일이 아니면 에러를 발생해 주세요.
에러 메시지는 "이메일이 아닙니다"로 해주세요.
이메일이면 이메일을 리턴해 주세요.
"""
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return email
    else:
        raise ValueError("이메일이 아닙니다")
