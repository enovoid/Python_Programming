import requests

BASE_URL = "https://huggingface.co/api/models"


def fetch_trending(limit=50):
    """지금 뜨는 모델 목록(API 원본)을 리스트로 돌려준다."""
    params = {"sort": "trendingScore", "direction": -1, "limit": limit}
    # TODO 1: requests.get으로 BASE_URL에 요청 (params, timeout=10)
    res = requests.get(BASE_URL, params=params, timeout=10)
    # TODO 2: 실패한 요청이면 예외 발생 (raise_for_status)
    res.raise_for_status()
    # TODO 3: JSON을 파이썬 리스트로 바꿔서 돌려주기
    return res.json()


def parse_model(raw):
    """API가 준 모델 하나(딕셔너리)에서 필요한 값만 남긴다."""
    # TODO: raw.get("키", 기본값)으로 하나씩 꺼내기
    return {
        "model_id": raw.get("id", ""),  # "id"
        "task": raw.get("pipeline_tag")
        or "unknown",  # "pipeline_tag" (없으면 "unknown")
        "downloads": raw.get("downloads", 0),  # "downloads" (없으면 0)
        "likes": raw.get("likes", 0),  # "likes" (없으면 0)
        "trending_score": raw.get("trendingScore", 0),  # "trendingScore" (없으면 0)
    }


def get_trending_models(limit=50):
    """가져오기 + 골라내기를 합친 함수. 다른 모듈은 이것만 쓴다."""
    # TODO: fetch_trending() 결과의 각 항목에 parse_model 적용
    return [parse_model(raw) for raw in fetch_trending(limit)]


if __name__ == "__main__":
    # 이 파일을 직접 실행했을 때만 동작하는 확인용 코드
    for m in get_trending_models(5):
        print(m)
