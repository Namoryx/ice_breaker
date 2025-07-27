<<<<<<< HEAD
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

information = """
기획사 아뮤즈에 스카웃되어 데뷔했다. 고교 2학년부터 3학년까지 1년간 가면라이더 덴오에서 주인공 노가미 료타로역을 맡아 1인 7역이라는 무시무시한 연기를 해 인기가 급상승했다. 실제 방송분에서 목소리는 노가미 료타로에게 빙의한 각각의 이매진 역을 맡은 성우들이 연기했지만, 그 목소리가 딱 어울리게 각 이매진에 맞춘 연기를 선보였다. 특히 덴오 3화에선 모모타로스에게 빙의된 상태를 본인의 목소리 그대로 연기했는데 위화감 없이 잘 어울리는 모습을 보여주었다.

덴오에서의 이미지를 간직하고 있는 팬들은 다시 노가미 료타로 역으로 덴오 극장판에 출연해주기를 기대하고 있지만, 덴오 극장판이 충분히 많이 나와 더이상의 덴오 극장판은 과할 뿐더러 2012년 9월 방한에서 앞으로 덴오는 힘들 거라고 확인 사살을 했다. 당시의 뉴타입 한국판 인터뷰를 보면 본인도 덴오 자체에 대한 애착도 있는 것으로 보인다. 본래는 극장판 3편 사라바 덴오에도 출연이 불투명했으나, 운이 좋았던 건지 당시 동시 촬영을 하고 있던 루키즈에서 혼자서만 배역이 가장 늦게 들어와서 여유롭게 덴오 극장판을 촬영했던 거라고. 루키즈의 히라카와 유이치로 감독이 말하길 무슨 역할을 시켜도 연기가 나쁘진 않았으나, "이거다!" 싶은 게 없어서 가장 배역이 늦게 돌아간 거라고 한다. 뭘 해도 무난했기에 이렇게 되면 무슨 역할을 맡겨도 캐릭터가 묻힐 거라고 판단했기 때문이라고. 사실 이후에도 안 나오는건 개런티보단 다른 스케쥴과의 조정 문제가 은근 크게 작용한다. 본인도 소속사도 다른 작품들로 연기를 넓혀가려는 목적이기도 하고. 이 때문에 더 이상 노가미 료타로서의 그를 볼 수 없을 것이라 생각하고 기대를 접었던 팬들에겐 놀랍게도 2018년 가면라이더 헤이세이 제네레이션즈 FOREVER에 노가미 료타로로서 출연했다. 비록 3분 남짓한 짧은 출연에 우라타로스가 빙의한 상태의 U료타로로서 출연[2]하긴 했지만 그 누구도 기대하지 않은 서프라이즈 출연에 팬들은 매우 기뻐했다. 사토가 연기한 료타로가 등장하자 관객석에서 환호가 터져나왔을 정도였으니... 이후 2023년에 한 인터뷰에서도 덴오뿐만이 아닌 다른 가면라이더를 또 찍을 의향이 있다고 하는 등 가면라이더 시리즈에 대한 애정을 드러낸 바 있다.

또한 한국에서는 바람의 검심 -메이지 검객 낭만기-의 히무라 켄신역으로 많이 알려져 있다. 그의 연기력은 실사판 영화중 가히 역대 최고라고 말할 수 있다. 또한 그가 보여준 켄신의 싱크로율은 말 그대로 켄신을 하기 위해 태어난 남자라고 칭할 만큼 원작의 켄신과 똑같은 모습을 보여준다. 바람의 검심 또한 5개의 시리즈 전부 다 흥행 대성공에 이르렀다. 그가 보여준 액션씬은 역대 검술 영화들 중 가장 최고의 액션씬을 보여줬다. 사토 타케루 본인도 켄신의 역할에 대해 애착이 매우 크며 후에 나온 마지막 시리즈인 바람의 검심 최종장 -THE FINAL/THE BEGINNINEG 촬영에 들어가기 앞서 목숨까지 던지겠다는등 바람의검심 시리즈 대한 애정을 보여주었고 또한 배우로써의 열정에 임하는 자세를 보여줬다.

2015년 10월 부산국제영화제 참석차 방한했다. 그리고 여기서 송강호와 우연히 마주치게 되었는데, 사토 타케루는 "송강호는 평소 존경하는 배우로 그의 작품도 많이 봐왔다. 이번 영화제에서 꼭 만나뵙고 싶었는데 실제로 만나게 돼 영광이었다. 나중에 꼭 같이 작품을 해보고 싶다."며 소감을 밝히기도 했다.

2017년 2월 23일, 덴오 10주년 이벤트에 나카무라 유이치와의 전화연결로 특별출연했다. 다른 배우들도 나온다는걸 알고 있었지만 가지 못해서 아쉽다고.

2017년 11월 29일, 일본에서 처음 열린 엠넷 음악축제 MAMA에 일본인 시상자로 참석했다. 서프라이즈라 한일 모두 실검에 오르기도 했다. 일본 연예계를 아는 사람들은 '사토 타케루같은 유명 배우가 굳이 여길?'이라는 반응이었고[3], 모르는 사람들은 '저 잘생긴 사람 누구냐?'라는 반응이었다. # 본인은 이런 글로벌 음악축제가 많아져서 국가간 거리가 좁혀졌으면 좋겠다는 소감을 밝혔다.

2018년 12월 31일, NHK 홍백가합전 심사위원으로 참석했다. mc들이 심사위원석에 앉은 사토 타케루 앞에서 계속 진행한 덕에 꽃병풍 역할을 톡톡히 했다.

2019년 4월 12일, 시리즈 누계 흥행 수입 125억엔 대히트 영화 바람의 검심 -메이지 검객 낭만기-의 신작 제작 소식을 발표했다. 촬영기간은 약 7개월(2018.11.04 - 2019.06.07)로 2020년 여름, 바람의 검심 -메이지 검객 낭만기- 최종장 2편 연속 개봉 예정(7월 3일 -THE FINAL / 8월 7일 -THE BEGINNINEG)이었으나 코로나19의 영향으로 2021년 GW(4월 23일 -THE FINAL / 6월 3일 -THE BEGINNINEG)로 개봉이 연기되었다. # 이후 개봉되어 두편모두 극찬을 받으며 나란히 흥행에 대성공해 뛰어난 흥행력을 발휘했다.

2020년 1분기 드라마 '사랑은 계속될 거야 어디까지나(恋はつづくよどこまでも[4])에 출연하여 2020년 여심을 휩쓸었다. 워낙 핫한 인기덕에 2020년 결산 일본 야후 검색대상을 받았다.# 대상과 남자배우 부문 2관왕. 도쿄드라마어워즈에선 남우조연상을 수상했다.#.

2021년 3월 31일부로 아뮤즈를 퇴사하며 새로운 사무소인 'Co-LaVo'를 설립해 이적했다
"""

if __name__ == "__main__":

    print("hello world")

    # Ensure the OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        raise EnvironmentError("The OPENAI_API_KEY environment variable is not set. Please set it before running this script.")

    summary_template = """
        given the information {information} about a person from I want to create :
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = summary_prompt_template | llm

    res = chain.invoke({"information": information})
    print(res)
=======
from typing import Tuple
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from chains.custom_chains import (
    get_summary_chain,
    get_interests_chain,
    get_ice_breaker_chain,
)
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets, scrape_user_tweets_mock
from output_parsers import (
    Summary,
    IceBreaker,
    TopicOfInterest,
)


def ice_break_with(
    name: str,
) -> Tuple[Summary, TopicOfInterest, IceBreaker, str]:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    twitter_username = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets_mock(username=twitter_username)

    summary_chain = get_summary_chain()
    summary_and_facts: Summary = summary_chain.invoke(
        input={"information": linkedin_data, "twitter_posts": tweets},
    )

    interests_chain = get_interests_chain()
    interests: TopicOfInterest = interests_chain.invoke(
        input={"information": linkedin_data, "twitter_posts": tweets}
    )

    ice_breaker_chain = get_ice_breaker_chain()
    ice_breakers: IceBreaker = ice_breaker_chain.invoke(
        input={"information": linkedin_data, "twitter_posts": tweets}
    )

    return (
        summary_and_facts,
        interests,
        ice_breakers,
        linkedin_data.get("photoUrl"),
    )


if __name__ == "__main__":
    pass
>>>>>>> 642938b6d67b2bd8bfa3bc46a15ef114b59d1900
