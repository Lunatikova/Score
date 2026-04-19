# app.py
import streamlit as st

# ------------------- Функция расчёта итоговой оценки -------------------
def calculate_grade(semester_grade, testing_grade, practical_grade, exam_grade,
                    w_sem, w_test, w_pract, w_exam):
    total = (semester_grade * w_sem + testing_grade * w_test +
             practical_grade * w_pract + exam_grade * w_exam) / 100
    return total

# ------------------- Интерфейс приложения -------------------
st.set_page_config(page_title="Калькулятор итоговой оценки", page_icon="🎓")
st.title("🎓 Калькулятор итоговой оценки")
st.markdown("Настройте оценки и веса — итоговая оценка пересчитывается автоматически.")

# Разделим на две колонки для удобства
col1, col2 = st.columns(2)

with col1:
    st.subheader("📚 Оценки (0–5)")
    semester_grade = st.slider("Семестровая оценка", 0.0, 5.0, 3.0, 0.1, format="%.2f")
    testing_grade = st.slider("Тестирование", 0, 5, 3, 1)          # целочисленный
    practical_grade = st.slider("Практический навык", 0.0, 5.0, 3.0, 0.1, format="%.2f")
    exam_grade = st.slider("Экзамен", 0, 5, 3, 1)                 # целочисленный

with col2:
    st.subheader("⚖️ Веса компонентов (%)")
    w_sem = st.slider("Вес семестра", 0, 100, 20)
    w_test = st.slider("Вес тестирования", 0, 100, 5)
    w_pract = st.slider("Вес практики", 0, 100, 15)
    w_exam = st.slider("Вес экзамена", 0, 100, 60)

# Расчёт
total_weight = w_sem + w_test + w_pract + w_exam
final_score = calculate_grade(semester_grade, testing_grade, practical_grade, exam_grade,
                              w_sem, w_test, w_pract, w_exam)

st.divider()
st.subheader("📊 Результат")

# Крупная метрика
st.metric("Итоговая оценка", f"{final_score:.2f}")

# Контроль суммы весов
if total_weight != 100:
    st.warning(f"⚠️ Сумма весов = {total_weight}%, а должна быть 100%")
else:
    st.success("✅ Сумма весов = 100%")

# Пояснение
with st.expander("ℹ️ Как это работает"):
    st.markdown("""
    Формула:  
    `(Семестр × вес_семестра + Тест × вес_теста + Практика × вес_практики + Экзамен × вес_экзамена) / 100`  
    Все оценки по 5-балльной шкале. Веса задаются в процентах, в сумме должны давать 100%.
    """)
