import tkinter as tk  # tkinter 모듈을 tk로 임포트
from tkinter import messagebox  # tkinter 모듈에서 messagebox만을 가져옴
from PIL import Image, ImageTk  # PIL 모듈에서 Image와 ImageTk를 가져옴
import random  # random 모듈을 임포트

# 나라 정보 데이터
countries = {   
    "easy": [        # 쉬운 난이도의 나라 정보
        {
            "name": "미국",
            "capital": "워싱턴 D.C.",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\쉬움\미국.png",
            "hint1": "수도: 워싱턴, 이 나라 때문에 우리가 영어를 배운다",
            "hint2": "자유의 여신상이 있다."
        },
        {
            "name": "이집트",
            "capital": "카이로",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\쉬움\이집트.png",
            "hint1": "수도: 카이로. 피라미드가 존재하고, 시신을 미라로 만들어 보관한다.",
            "hint2": "아프리카에 위치하고 살라의 나라이다."
        },
        {
            "name": "영국",
            "capital": "런던",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\쉬움\영국.png",
            "hint1": "수도: 런던. 축구 국가대표 손흥민이 뛰고 있는 팀이 소속된 나라이다.",
            "hint2": "하나의 독립적인 나라가 아니라 4개의 나라가 합쳐진 연맹국가이다."
        },
        {
            "name": "캐나다",
            "capital": "오타와",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\쉬움\캐나다.png",
            "hint1":"수도: 오타와. 사계절이 춥고 단풍잎이 유명하다.",
            "hint2": "다문화국가라서 다양한 인종이 살고 있다."
        },
        {
            "name": "이탈리아",
            "capital": "로마",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\쉬움\이탈리아.png",
            "hint1": "수도: 로마. 파스타와 피자의 나라이다.",
            "hint2": "인종차별이 심한 나라로 알려져 있다."
        },
        {
            "name": "프랑스",
            "capital": "파리",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\쉬움\프랑스.png",
            "hint1": "수도: 파리. 에펠탑이 있다.",
            "hint2": "이 나라 사람들은 자기네 언어에 자부심을 크게 느끼고 있다."
        },
        {
            "name": "우루과이",
            "capital": "몬테비데오",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\쉬움\우루과이.png",
            "hint1": "수도: 몬테비데오, 남미에 위치해 있으며 스페인어를 사용하고 백인의 비율이 굉장히 높다",
            "hint2": "2022 카타르 월드컵에서 우리나라와 조별리그 때 첫경기를 치뤘던 나라이다."
        },
        {
            "name": "인도네시아",
            "capital": "자카르타.",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\쉬움\인도네시아.png",
            "hint1": "수도: 자카르타. 동남아시아에 위치해 있으며 세계에서 4번째로 인구가 많은 나라다",
            "hint2": "신혼 여행으로 유명한 발리가 있는 나라다"
        },
        {
            "name": "호주",
            "capital": "캔버라",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\쉬움\호주.png",
            "hint1": "수도: 캔버라. 유명한 오페라 하우스, 멜버른, 브리즈번, 시드니 등의 도시가 있는 나라이다.",
            "hint2": "상어가 많이 출현해 상어에게 물림 사망사고가 많이 발생하는 나라이다."
        },
        {
            "name": "필리핀",
            "capital": "마닐라",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\쉬움\필리핀.png",
            "hint1": "수도: 마닐라. 동남아시아에 위치해 있으며, 미국의 식민지배를 받아 총기소지가 허용된 국가이고 아시아에서 치안이 가장 좋지 않은 국가 중 하나이다.",
            "hint2": "보라카이 섬, 세부 등 여행하기 좋은 섬들이 있는 나라이다."
        },
    ],
    "medium": [     # 보통 난이도의 나라 정보
        {
            "name": "멕시코",
            "capital": "멕시코시티",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\보통\멕시코.png",
            "hint1": "또띠아의 나라이다.",
            "hint2": "북아메리카와 남아메리카 중간에 위치해 있다."
        },
        {
            "name": "아르헨티나",
            "capital": "부에노스아이레스",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\보통\아르헨티나.png",
            "hint1": "수도: 부에노스아이레스. 남아메리카에서 2번째로 큰 나라이다.",
            "hint2": "메시의 나라이다."
        },
        {
            "name": "싱가포르",
            "capital": None,
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\보통\싱가포르.png",
            "hint1": "도시국가이고 동남아시아에 위치해 있다.",
            "hint2": "6/6(목)에 우리나라가 국가대표 축구 경기에서 7:0으로 이긴 나라다."
        },
        {
            "name": "베트남",
            "capital": "하노이",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\보통\베트남.png",
            "hint1": "수도: 하노이. 사계절 비가 오고 습하고, 쌀국수가 유명하다.",
            "hint2": "예전 1900년대에 이 나라 전쟁에 우리나라가 참전했었다."
        },
        {
            "name": "포르투갈",
            "capital": "리스본",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\보통\포르투갈.png",
            "hint1": "수도: 리스본. 호날두의 나라이다.",
            "hint2": "대한민국에서 비행기로 가장 오래 걸리는 나라이다."
        },
        {
            "name": "대만",
            "capital": "타이베이",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\보통\대만.png",
            "hint1": "수도: 타이베이, 동남아시아에 위치해 있으며, 열대 과일(망고, 망고스틴 등)과 우육면, 딤섬 등 먹을거리가 유명한 나라이다",
            "hint2": "2010까지 세계에서 가장 높은 빌딩인 타이베이 101과 스린 야시장 등이 관광 명소이다."
        },
        {
            "name": "칠레",
            "capital": "산티아고",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\보통\칠레.png",
            "hint1": "수도: 산티아고, 남미에 위치햇으며 남북으로 길고 가늘게 쭉 뻗어있는 특이한 형태의 영토 모양으로 유명하다 ",
            "hint2": "이스터 섬에 있는 모아이 석상이 유명하다"
        },
        {
            "name": "태국",
            "capital": "방콕",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\보통\태국.png",
            "hint1": "수도: 방콕, 동남아시아에 위치해 있으며, 뚬양꿍, 팟타이, 코코넛 커리 국수 등 먹거리가 유명하다",
            "hint2": "관광지로 방콕, 치앙마이, 푸켓 등이 유명하다"
        },
        {
            "name": "이스라엘",
            "capital": "예루살렘",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\보통\이스라엘.png",
            "hint1": "수도: 예루살렘, 서남아시아에 위치해 있으며 현재 전쟁 진행중인 나라이다.",
            "hint2": "종교의 비율이 유대인 80프로, 이슬람 20프로이다. 예루살렘은 기독교의 성지이다"
        },
        {
            "name": "베네수엘라",
            "capital": "카라카스",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\보통\베네수엘라.png",
            "hint1": "수도: 카라카스, 남미에 위치해 있으며, 세계 원유매장령 1위 국가 대규모 석유수출을 해온 1세대 산유국이다.",
            "hint2": "과도한 원유 의존 경제에다 정부의 실책 및 비리가 결합하여 2019년 경제 대위기가 찾아왔다. 순식간에 산유국에서 밑바닥 국가로 전락하고 말았다."
        },
    ],
    "hard": [       # 어려운 난이도의 나라 정보
        {
            "name": "오스트리아",
            "capital": "빈",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\어려움\오스트리아.png",
            "hint1": "수도: 빈. 독일, 스위스와 붙어 있고 나라의 80퍼센트 이상이 알프스 산맥으로 뒤덮여 있다.",
            "hint2": "모차르트와 베토벤의 나라이다."
        },
        {
            "name": "체코",
            "capital": "프라하",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\어려움\체코.png",
            "hint1": "수도: 프라하. 프라하성, 성 비투스 대성당 등 아름다운 성이 많다. 참고로 프라하 성은 세계에서 가장 큰 옛 성이다.",
            "hint2": "독일과 함께 흑맥주가 유명하고 카를교에서 커플들의 사랑이 이루어진다는 소문이 있다."
        },
        {
            "name": "알제리",
            "capital": "알제",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\어려움\알제리.png",
            "hint1": "수도: 알제. 지중해에 위치하며, 프랑스의 지배를 받아 프랑스어를 사용한다.",
            "hint2": "2014 브라질 월드컵 때 우리나라와 붙어 우리에게 4:2의 패배를 안겨줬던 나라이다."
        },
          {
            "name": "콜롬비아",
            "capital": "보고타",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\어려움\콜롬비아.png",
            "hint1": "수도: 보고타. 커피(원두)로 유명하고 석유가 많이 나온다.",
            "hint2": "마약과 범죄로 유명해 여행이 제한되는 나라이다."
        },
          {
            "name": "벨기에",
            "capital": "브뤼셀",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\어려움\벨기에.png",
            "hint1": "수도: 브뤼셀. 초콜릿, 와플, 등 디저트가 유명하다.",
            "hint2": "2018 러시아 월드컵에서 우리나라에게 1대0 패배를 안겨준 나라이다.."
        },
        {
            "name": "부탄",
            "capital": "팀부",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\어려움\부탄.png",
            "hint1": "수도: 팀부, 남아시아에 위치해 있으며, 효율과 편리라는 기치 아래 경제성장에 목을 맬 때도, GNH(국민총행복지수)를 최고 정책으로 삼고 있는 나라이다.",
            "hint2": "지구상에서 환경보호에 가장 민감하며, 영적인 것에 깊은 관심을 기울이는 나라이다.(ex, 새들의 목에 줄이 걸릴까 염려되어 전깃줄을 잇지 않는 나라)"
        },
        {
            "name": "수리남",
            "capital": "파라마리보",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\어려움\수리남.png",
            "hint1": "수도: 파라마리보, 남미에 위치해 있으며, 산림이 국토의 95%를 덮고 있어 세계 최고 수준이다. 국토의 대부분을 열대우림이 덮고 있다.",
            "hint2": "우리나라에서 이 나라가 영화 이름인 영화를 개봉한 적이 있다. 황정민 배우가 출현햇었다."
        },
        {
            "name": "네덜란드",
            "capital": "암스테르담",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\어려움\네덜란드.png",
            "hint1": "수도: 암스테르담, 서유럽에 위치해 잇으며, 풍차와 튤립이 유명한 나라이다",
            "hint2": "세계에서 키가 가장 큰 나리아다. 남자 평균: 195cm, 여자 평균: 180cm"
        },
        {
            "name": "요르단",
            "capital": "암만",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\어려움\요르단.png",
            "hint1": "수도: 암만. 중동에 위치해 있으며, 권위주의 국가이며 심각한 언론 탄압국으로 지정되어 있다.",
            "hint2": "이번 2024 남자 축구 아시안컵 준결승전에서  우리나라가 이 나라에게 떨어졌다."
        },
        {
            "name": "헝가리",
            "capital": "부다페스트",
            "flag": r"C:\Users\p0418\Desktop\컴퓨터공학과 2학년 1학기\고급파이썬프로그래밍\16주차(과제 발표)\과제\나라 국기\어려움\헝가리.png",
            "hint1": "수도: 부다페스트. 동유럽에 위치해 있으며, 밤에 국회의사당 야경이 최고의 인기 여행지이다.",
            "hint2": "부다 성, 국회의사당, 성 이슈트반 대성당, 어부의 요새 등이 관광지로 유명하다. "
        }
    ]
}

class CountryGuessingGame:
    def __init__(self, root):
        self.root = root  # Tk 객체 저장
        self.root.title("나라 맞추기 게임")  # 윈도우 제목 설정

        # 초기화
        self.score = 0  # 점수
        self.rounds = 0  # 현재 라운드
        self.max_rounds = 10  # 총 라운드 수
        self.hint1_count = 0  # 힌트 1 사용 횟수
        self.hint2_count = 0  # 힌트 2 사용 횟수
        self.hint_count = 0  # 힌트 사용 총 횟수
        self.max_hint_count = 20  # 최대 힌트 사용 횟수

        self.difficulty = None  # 선택된 난이도
        self.instructions_window = None  # 게임 방법 창을 위한 변수
        self.difficulty_window = None  # 난이도 선택 창을 위한 변수
        self.create_widgets()  # 위젯 생성
        self.show_instructions()  # 게임 방법 창 표시
        self.show_difficulty_selection()  # 난이도 선택 창 표시
        self.selected_countries = set()  # 중복된 나라를 방지하기 위한 집합
        self.used_countries = {  # 사용된 나라 기록
            "easy": [],
            "medium": [],
            "hard": []
        }
        self.easy_countries = countries["easy"]  # 쉬운 난이도의 나라 정보
        self.medium_countries = countries["medium"]  # 보통 난이도의 나라 정보
        self.hard_countries = countries["hard"]  # 어려운 난이도의 나라 정보


    # 게임 방법 창 표시
    def show_instructions(self):
        self.instructions_window = tk.Toplevel(self.root)  # Toplevel 창 생성
        self.instructions_window.title("게임 방법")  # 창 제목 설정
        
        # 게임 방법 텍스트 설정
        instructions_text = """ 
<게임 방법>
1) 주어진 나라의 국기를 기반으로 어떤 나라인지 맞춘다.
2) 난이도 별로 문제가 다르고 총 5문제씩 출제되어 있다.
3) 문제를 맞출 때마다 20점씩 점수를 얻는다.
4) 각 문제마다 힌트가 2개까지 주어지고 힌트2는 힌트1을 봐야지만 볼 수 있다
5) 힌트2가 좀 더 명확한 힌트이다.
6) 힌트1이든 힌트2이든 5문제 중에서 3번 보면 점수가 10점 깎인다.
7) 힌트를 4번 또는 5번 보면 점수가 5점 더 깍인다. 
8) 힌트를 6번 보면 추가적으로 5점이 깎여 전체 20점이 깎인다.
9) 힌트 사용 횟수와 점수는 화면에 즉시적으로 표시된다.
10) 힌트1은 그 나라의 수도와 특징에 대해서 나와있다.
"""
        # 게임 안내 메시지 라벨 생성 후 패킹
        tk.Label(self.instructions_window, text=instructions_text, font=("맑은 고딕", 14)).pack(pady=20)

        # 게임 시작 버튼 생성 후 패킹
        self.start_game_button = tk.Button(self.instructions_window, text="게임 시작", command=self.show_difficulty_selection)
        self.start_game_button.pack(pady=10)
        
    def create_widgets(self):   # 위젯 생성 메서드
        # 나라 정보를 표시하는 라벨 생성 후 패킹
        self.info_label = tk.Label(self.root, text="나라 정보를 확인하세요!", font=("맑은 고딕", 14))
        self.info_label.pack(pady=20)

        # 국기 이미지를 표시하는 라벨 생성 후 패킹
        self.flag_label = tk.Label(self.root)
        self.flag_label.pack(pady=20)

         # 힌트 1을 보는 버튼 생성 후 패킹
        self.hint1_button = tk.Button(self.root, text="힌트 1 보기", command=self.show_hint1)
        self.hint1_button.pack(pady=10)

        # 힌트 2을 보는 버튼 생성 후 패킹
        self.hint2_button = tk.Button(self.root, text="힌트 2 보기", command=self.show_hint2)
        self.hint2_button.pack(pady=10)
        self.hint2_button.config(state=tk.DISABLED)

        # 정답을 입력하는 엔트리 위젯 생성 후 패킹
        self.guess_entry = tk.Entry(self.root, font=("맑은 고딕", 14))
        self.guess_entry.pack(pady=10)

        # 현재 점수를 표시하는 라벨 생성 후 패킹
        self.score_label = tk.Label(self.root, text="점수: 0", font=("맑은 고딕", 14))
        self.score_label.pack(pady=10)

        # 힌트 사용 횟수를 표시하는 라벨 생성 후 패킹
        self.hint_count_label = tk.Label(self.root, text="힌트 사용 횟수: 0", font=("맑은 고딕", 14))
        self.hint_count_label.pack(pady=10)

        # 정답을 제출하는 버튼 생성 후 패킹
        self.submit_button = tk.Button(self.root, text="제출", command=self.check_answer)
        self.submit_button.pack(pady=10)

        # 결과를 표시하는 라벨 생성 후 패킹
        self.result_label = tk.Label(self.root, text="", font=("맑은 고딕", 14))
        self.result_label.pack(pady=20)


    def show_difficulty_selection(self):     # 난이도 선택 창을 보여주는 메서드
        # 난이도 선택 창 생성
        self.difficulty_window = tk.Toplevel(self.instructions_window)
        self.difficulty_window.title("난이도 선택")

        # 난이도 선택 안내 메시지 라벨 생성 후 패킹
        tk.Label(self.difficulty_window, text="난이도를 선택하세요:", font=("맑은 고딕", 14)).pack(pady=20)

        # 쉬움, 보통, 어려움 버튼 생성 후 패킹, 클릭 시 set_difficulty 메서드 호출
        tk.Button(self.difficulty_window, text="쉬움", command=lambda: self.set_difficulty("easy")).pack(pady=10)
        tk.Button(self.difficulty_window, text="보통", command=lambda: self.set_difficulty("medium")).pack(pady=10)
        tk.Button(self.difficulty_window, text="어려움", command=lambda: self.set_difficulty("hard")).pack(pady=10)

    # 난이도를 설정하는 메서드
    def set_difficulty(self, difficulty):
        # 선택한 난이도 설정
        self.difficulty = difficulty
        # 난이도 선택 창 닫기
        self.difficulty_window.destroy()
        # 다음 라운드 시작
        self.next_round()

    # 다음 라운드를 시작하는 메서드
    def next_round(self):
        # 현재 라운드가 최대 라운드보다 작은 경우에만 실행
        if self.rounds < self.max_rounds:
            # 이전에 선택된 나라들과 중복되지 않는 새로운 나라 선택
            if self.difficulty == "easy":
                country_list = [c for c in self.easy_countries if c["name"] not in self.selected_countries]
            elif self.difficulty == "medium":
                country_list = [c for c in self.medium_countries if c["name"] not in self.selected_countries]
            elif self.difficulty == "hard":
                country_list = [c for c in self.hard_countries if c["name"] not in self.selected_countries]

            # 모든 국가를 사용한 경우 선택된 국가 기록 초기화하고 나라 리스트 초기화
            if not country_list:
                self.selected_countries.clear()
                if self.difficulty == "easy":
                    country_list = self.easy_countries
                elif self.difficulty == "medium":
                    country_list = self.medium_countries
                elif self.difficulty == "hard":
                    country_list = self.hard_countries

                random.shuffle(country_list)

            # 현재 라운드의 나라 선택
            self.current_country = random.choice(country_list)
            self.selected_countries.add(self.current_country["name"])  # 선택된 나라 기록

            # 국기 이미지 표시
            flag_image = Image.open(self.current_country["flag"])
            flag_image = flag_image.resize((150, 100), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.LANCZOS)
            self.flag_image = ImageTk.PhotoImage(flag_image)
            self.flag_label.config(image=self.flag_image)

            # 엔트리 초기화, 결과 라벨 초기화, 힌트2 버튼 비활성화
            self.guess_entry.delete(0, tk.END)
            self.result_label.config(text="")
            self.hint2_button.config(state=tk.DISABLED)
            self.rounds += 1
        else:
            # 게임 종료
            self.end_game()

    # 힌트1을 보여주는 메서드
    def show_hint1(self):
        # 최대 힌트 사용 횟수보다 작을 때만 힌트 표시
        if self.hint_count < self.max_hint_count:
            messagebox.showinfo("힌트 1", self.current_country["hint1"])
            self.hint_count += 1  # 힌트 사용 횟수 증가
            self.hint2_button.config(state=tk.NORMAL)  # 힌트2 버튼 활성화
            self.hint_count_label.config(text=f"힌트 사용 횟수: {self.hint_count}")  # 힌트 사용 횟수 표시

            # 힌트 사용 횟수에 따라 점수 감점
            if self.hint_count == 3:
                self.score -= 10
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 4 or self.hint_count == 5:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 6:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 7 or self.hint_count == 8:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 9:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 10 or self.hint_count == 11:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 12:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 13 or self.hint_count == 14:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 15:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 16 or self.hint_count == 17:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 18:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 19 or self.hint_count == 20:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            

    # 힌트2를 보여주는 메서드
    def show_hint2(self):
        # 최대 힌트 사용 횟수보다 작을 때만 힌트 표시
        if self.hint_count < self.max_hint_count:
            messagebox.showinfo("힌트 2", self.current_country["hint2"])
            self.hint_count += 1  # 힌트 사용 횟수 증가
            self.hint_count_label.config(text=f"힌트 사용 횟수: {self.hint_count}")  # 힌트 사용 횟수 표시

            # 힌트 사용 횟수에 따라 점수 감점
            if self.hint_count == 3:
                self.score -= 10
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 4 or self.hint_count == 5:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 6:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 7 or self.hint_count == 8:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 9:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 10 or self.hint_count == 11:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 12:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 13 or self.hint_count == 14:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 15:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 16 or self.hint_count == 17:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 18:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트
            elif self.hint_count == 19 or self.hint_count == 20:
                self.score -= 5
                self.score_label.config(text=f"점수: {self.score}")  # 점수 감점 후 라벨 업데이트

    def check_answer(self):     # 정답을 확인하는 메서드
     # 사용자가 입력한 정답
        guess = self.guess_entry.get().strip()
        
        # 정답 확인
        if guess == self.current_country["name"]:
            self.score += 10  # 정답 시 10점 추가
            self.result_label.config(text="정답입니다!", fg="green")
        else:
            self.result_label.config(text=f"오답입니다! 정답은 {self.current_country['name']}입니다.", fg="red")
        
        # 힌트 사용 횟수에 따라 점수 감점
        if self.hint1_count > 2:
            self.score -= 10  # 힌트 1을 3번 이상 사용하면 10점 감점
        if self.hint2_count > 2:
            self.score -= 10  # 힌트 2를 3번 이상 사용하면 10점 감점

        # 점수를 라벨에 업데이트
        self.score_label.config(text=f"점수: {self.score}")

        # 다음 라운드 시작
        self.root.after(2000, self.next_round)

    # 게임 종료 메서드
    def end_game(self):
        # 점수 백분율 계산
        score_percentage = (self.score / (self.max_rounds * 10)) * 100
        # 게임 종료 메시지 박스 표시
        result = messagebox.showinfo("게임 종료", f"게임이 끝났습니다!\n점수: {self.score}/{self.max_rounds*10} ({score_percentage:.0f}%)")
        if result == 'ok':
            # 게임 리셋
            self.reset_game()

    # 게임 리셋 메서드
    def reset_game(self):
        # 점수, 라운드, 힌트 사용 횟수 초기화
        self.score = 0
        self.rounds = 0
        self.hint1_count = 0
        self.hint2_count = 0
        self.selected_countries.clear()  # 기존에 선택된 나라들 초기화
        # 난이도 선택 창 다시 보여주기
        self.show_difficulty_selection()

# Tk 객체 생성
root = tk.Tk()
# CountryGuessingGame 객체 생성
game = CountryGuessingGame(root)
# Tk 객체 이벤트 루프 시작
root.mainloop()
