from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="다은이의 첫 번째 서버", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def 메인페이지():
    return {"message": "안녕하세요! 제 서버에 오신 것을 환영합니다~🎉"}

@app.get("/ping")
def 서버_상태_확인():
    return {
        "message": "pong!🏓 서버 정상 작동 중~",
        "status" : "정상 작동 중"
    }

@app.get("/items")
def 상품_목록_가져오기():
    우리_가게_상품들 = [
        {"id": 1, "name": "게이밍 노트북", "price": 1200000, "category": "전자제품"},
        {"id": 2, "name": "기계식 키보드", "price": 150000, "category": "전자제품"},
        {"id": 3, "name": "게이밍 마우스", "price": 80000, "category": "전자제품"},
        {"id": 4, "name": "27인치 모니터", "price": 300000, "category": "전자제품"},
        {"id": 5, "name": "높이 조절 책상", "price": 200000, "category": "가구"}
    ]

    return {
        "items": 우리_가게_상품들,
        "count": len(우리_가게_상품들),
        "message": f"저희 가게에는 총 {len(우리_가게_상품들)}개의 상품이 있어요!"
    }

@app.get("/items/{item_id}")
def 특정_상품_찾기(item_id: int):
    우리_가게_상품들 = [
        {"id": 1, "name": "게이밍 노트북", "price": 1200000, "category": "전자제품"},
        {"id": 2, "name": "기계식 키보드", "price": 150000, "category": "전자제품"},
        {"id": 3, "name": "게이밍 마우스", "price": 80000, "category": "전자제품"},
        {"id": 4, "name": "27인치 모니터", "price": 300000, "category": "전자제품"},
        {"id": 5, "name": "높이 조절 책상", "price": 200000, "category": "가구"}
    ]

    for 상품 in 우리_가게_상품들:
        if 상품["id"] == item_id:
            return {
                "item": 상품,
                "message": f"{상품['name']}을(를) 찾았어요!"
            }
    
    return {
        "error": f"{item_id}번 상품을 찾을 수 없어요..😓",
        "message": "다른 번호로 다시 시도해보세요!🤔"
    }

@app.get("/search")
def 상품_검색하기(q: str = ""):
    모든_상품 = [
        {"id": 1, "name": "게이밍 노트북", "price": 1200000},
        {"id": 2, "name": "기계식 키보드", "price": 150000},
        {"id": 3, "name": "게이밍 마우스", "price": 80000},
        {"id": 4, "name": "27인치 모니터", "price": 300000},
        {"id": 5, "name": "높이 조절 책상", "price": 200000},
    ]

    if not q:
        return {
            "items": 모든_상품,
            "message": "저희 가게의 모든 상품을 모두 보여드릴게요~🤗",
            "search_term": "전체"
        }

    찾은_상품 = []
    for 상품 in 모든_상품:
        if q in 상품["name"]:
            찾은_상품.append(상품)
    
    return {
        "items": 찾은_상품,
        "count": len(찾은_상품),
        "search_term": q,
        "message": f"'{q}' (으)로 검색한 결과, 상품 {len(찾은_상품)}개를 찾았어요!🥳"
    }
