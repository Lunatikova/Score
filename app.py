# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:49:44 2026   D:/Python/2026

@author: Наташа
"""

import streamlit as st

# ------------------- Функция расчёта итоговой оценки -------------------
def calculate_grade(semester_grade, testing_grade, practical_grade, exam_grade,
                    w_sem, w_test, w_pract, w_exam):
    total = (semester_grade * w_sem + testing_grade * w_test +
             practical_grade * w_pract + exam_grade * w_exam) / 100
    return total

# ------------------- Заголовок и описание -------------------
st.set_page_config(page_title="Калькулятор итоговой оценки", page_icon="🎓")
st.title("🎓 Калькулятор итоговой оценки")
st.markdown("Настройте оценки и веса компонентов – итоговая оценка пересчитывается автоматически.")

# ------------------- Оценки -------------------
st.subheader("📚 Оценки (0–5)")

col1, col2 = st.columns(2)
with col1:
    semester_grade = st.slider("Семестровая оценка", 0.0, 5.0, 3.0, 0.1, format="%.2f")
    testing_grade = st.slider("Тестирование", 0, 5, 3, 1)   # целое
with col2:
    practical_grade = st.slider("Практический навык", 0.0, 5.0, 3.0, 0.1, format="%.2f")
    exam_grade = st.slider("Экзамен", 0, 5, 3, 1)          # целое

# ------------------- Веса -------------------
st.subheader("⚖️ Веса компонентов (%)")
col3, col4 = st.columns(2)
with col3:
    w_sem = st.slider("Вес семестра", 0, 100, 20)
    w_test = st.slider("Вес тестирования", 0, 100, 5)
with col4:
    w_pract = st.slider("Вес практики", 0, 100, 15)
    w_exam = st.slider("Вес экзамена", 0, 100, 60)

# ------------------- Расчёт и вывод -------------------
total_weight = w_sem + w_test + w_pract + w_exam
final_score = calculate_grade(semester_grade, testing_grade, practical_grade, exam_grade,
                              w_sem, w_test, w_pract, w_exam)

st.divider()
st.subheader("📊 Результат")

# Крупный вывод итоговой оценки
st.metric("Итоговая оценка", f"{final_score:.2f}")

# Контроль суммы весов
if total_weight != 100:
    st.warning(f"⚠️ Сумма весов = {total_weight}%, а должна быть 100%")
else:
    st.success("✅ Сумма весов = 100%")
