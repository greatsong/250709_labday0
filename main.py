import streamlit as st

st.set_page_config(page_title="MBTI 직업 추천", page_icon="🔍")

st.title("🌟 MBTI 기반 직업 추천 앱")
st.write("당신의 MBTI를 선택하면 어울리는 직업과 피해야 할 직업을 알려드릴게요!")

# MBTI 직업 추천 딕셔너리
mbti_jobs = {
    "INTJ": {
        "emoji": "🧠📘📐♟️🌑",
        "추천직업": ["데이터 과학자", "전략 기획자", "시스템 설계자"],
        "비추천직업": ["판매원", "콜센터 상담원"],
        "이유": "논리적 사고와 독립적인 업무를 선호하여 복잡한 문제 해결에 강점을 가지나 반복적인 대인 관계에는 피로감을 느낄 수 있어요."
    },
    "INFP": {
        "emoji": "🦄📖🕯️🎼🌻",
        "추천직업": ["작가", "상담사", "디자이너"],
        "비추천직업": ["경찰", "회계사"],
        "이유": "이상주의적이고 감성적인 성향이 강해 창의성이 요구되는 직업에 어울리며, 규칙적인 시스템보다는 자유로운 환경을 선호해요."
    },
    "ESTJ": {
        "emoji": "📊💼🛠️📈🔧",
        "추천직업": ["경영 관리자", "공무원", "군인"],
        "비추천직업": ["프리랜서", "예술가"],
        "이유": "체계적이고 책임감이 강하여 조직 내 리더십을 발휘하는 데 탁월하지만, 유동적인 환경은 스트레스를 유발할 수 있어요."
    },
    "ENFP": {
        "emoji": "🌈✨🎨🧠🎉",
        "추천직업": ["기획자", "마케터", "심리상담사"],
        "비추천직업": ["경리", "자료입력원"],
        "이유": "창의적이고 사람과의 소통을 즐기는 성향이 강해 활발한 환경에서 에너지를 발휘해요. 반복적인 일은 금방 지루해질 수 있어요."
    },
    # 필요한 경우 다른 MBTI도 추가로 정의 가능
}

mbti_list = list(mbti_jobs.keys())

# 사용자 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

if selected_mbti:
    st.balloons()  # 풍선 효과
    data = mbti_jobs[selected_mbti]
    st.header(f"{selected_mbti} {data['emoji']}")
    
    st.subheader("✅ 추천 직업")
    for job in data["추천직업"]:
        st.write(f"💼 {job}")
    
    st.subheader("🚫 피해야 할 직업")
    for job in data["비추천직업"]:
        st.write(f"❌ {job}")
    
    st.subheader("🧾 이유")
    st.write(data["이유"])
