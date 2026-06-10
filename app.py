import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="碳智·浚浦",
    page_icon="🚢",
    layout="wide"
)

# ======================
# 全局数据库
# ======================

quota = {

    # 40
    ("40", "I-II类土"): 167.59,
    ("40", "III类土"): 223.45,
    ("40", "IV类土"): 268.14,
    ("40", "细粉砂"): 201.11,

    # 80
    ("80", "I-II类土"): 77.32,
    ("80", "III类土"): 103.09,
    ("80", "IV类土"): 123.71,
    ("80", "V类土"): 175.25,
    ("80", "VI类土"): 237.11,
    ("80", "松散中砂"): 155.58,
    ("80", "中密中砂"): 178.92,
    ("80", "粗砂"): 182.02,

    # 120
    ("120", "I-II类土"): 60.00,
    ("120", "III类土"): 80.00,
    ("120", "IV类土"): 96.00,
    ("120", "V类土"): 136.00,
    ("120", "VI类土"): 184.00,
    ("120", "松散中砂"): 119.06,
    ("120", "中密中砂"): 136.92,
    ("120", "粗砂"): 139.32,

    # 200
    ("200", "I-II类土"): 31.14,
    ("200", "III类土"): 41.51,
    ("200", "IV类土"): 49.81,
    ("200", "V类土"): 70.57,
    ("200", "VI类土"): 95.47,
    ("200", "松散中砂"): 58.84,
    ("200", "中密中砂"): 67.67,
    ("200", "粗砂"): 68.84,

    # 350
    ("350", "I-II类土"): 17.09,
    ("350", "III类土"): 22.78,
    ("350", "IV类土"): 26.20,
    ("350", "V类土"): 34.17,
    ("350", "VI类土"): 47.84,
    ("350", "中砂"): 32.28,
    ("350", "粗砂"): 37.78,

    # 500
    ("500", "I-II类土"): 12.68,
    ("500", "III类土"): 16.90,
    ("500", "IV类土"): 19.44,
    ("500", "V类土"): 25.35,
    ("500", "VI类土"): 35.49,
    ("500", "VII类土"): 52.39,
    ("500", "松散中砂"): 23.96,
    ("500", "中密中砂"): 27.55,
    ("500", "紧密中砂"): 35.94,
    ("500", "粗砂"): 28.03,

    # 1450
    ("1450", "I-II类土"): 13.38,
    ("1450", "III类土"): 15.38,
    ("1450", "IV类土"): 16.92,
    ("1450", "V类土"): 20.30,
    ("1450", "VI类土"): 26.45,
    ("1450", "VII类土"): 37.06,
    ("1450", "松散中砂"): 17.00,
    ("1450", "中密中砂"): 18.87,
    ("1450", "紧密中砂"): 25.50,
    ("1450", "松散粗砂"): 17.59,
    ("1450", "中密粗砂"): 19.53,
    ("1450", "紧密粗砂"): 26.39,
}

# ======================
# 客观影响系数
# ======================

impact_factor = {
    "一级": 1.00,
    "二级": 1.07,
    "三级": 1.14,
    "四级": 1.23,
    "五级": 1.33,
    "六级": 1.45,
    "七级": 1.60
}

# ======================
# 船型油耗数据库
# kg/h
# ======================

oil_rate = {

    "40": 14,
    "80": 26,
    "120": 44,
    "200": 74,
    "350": 134,
    "500": 191,
    "1450": 438

}

if "page" not in st.session_state:
    st.session_state.page = "home"

# ======================
# 首页
# ======================

if st.session_state.page == "home":

    st.title("🚢 碳智·浚浦")

    st.markdown("### 航道疏浚作业低碳优化与碳资产核算平台")

    st.markdown("---")

    st.subheader("👨‍💻 项目团队")

    st.write("碳路者·EcoDredge")

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(
        ["作业现场1","作业现场2","作业现场3"]
    )

    with tab1:
        st.image("image1.jpg")

    with tab2:
        st.image("image2.jpg")

    with tab3:
        st.image("image3.jpg")
    st.markdown("## 📖 平台简介")

    st.write(
        """
        碳智·浚浦是一款面向航道疏浚工程的
        低碳优化决策与碳资产核算平台。

        平台结合工程量、土质条件、
        船型参数等关键数据，

        实现：

        ✅ 工期预测

        ✅ 碳排放核算

        ✅ 成本分析

        ✅ 最优船型推荐

        ✅ 低碳决策支持
        """
    )

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "🚀 简洁版",
            use_container_width=True
        ):
            st.session_state.page = "simple"
            st.rerun()

    with c2:

        if st.button(
            "✨ 精装版",
            use_container_width=True
        ):
            st.session_state.page = "pro"
            st.rerun()

    st.stop()

if st.session_state.page == "simple":
# ======================
# 标题
# ======================

    st.title("🚢 碳智·浚浦")
    st.subheader("航道疏浚作业低碳优化与碳资产核算平台")

    st.markdown("---")

    # ======================
    # 输入区域
    # ======================

    col1, col2 = st.columns(2)

    with col1:

        workload = st.number_input(
            "工程量（m³）",
            min_value=10000,
            value=100000,
            step=10000
        )

        ship_type = st.selectbox(
            "船型（m³/h）",
            ["40", "80", "120", "200", "350", "500", "1450"]
        )

    with col2:

        soil_type = st.selectbox(
            "土质类型",
            sorted(list(set([x[1] for x in quota.keys()])))
        )

        impact_level = st.selectbox(
            "客观影响等级",
            ["一级", "二级", "三级", "四级", "五级", "六级", "七级"]
        )
        opt_mode = st.selectbox(
            "优化目标",
            [
                "最低碳排放",
                "最短工期",
                "综合优化（推荐）"
            ]
        )
        
        target_days = st.number_input(
            "工期要求（天）",
            min_value=1,
            value=30,
            step=1
        )

    # ======================
    # 开始分析
    # ======================

    if st.button("开始分析"):

        if (ship_type, soil_type) not in quota:

            st.error("当前船型没有该土质定额数据！")

        else:

            # 定额台时
            unit_hour = quota[(ship_type, soil_type)]

            # 客观影响修正
            factor = impact_factor[impact_level]

            unit_hour = unit_hour * factor

            # 总施工台时
            total_hour = workload / 10000 * unit_hour

            # 工期
            daily_hour = 20
            days = total_hour / daily_hour

            # 实际油耗
            oil_per_hour = oil_rate[ship_type] / 1000
            total_oil = total_hour * oil_per_hour

            # 碳排放
            carbon = total_oil * 3.114

            # 燃油成本
            diesel_price = 8500
            fuel_cost = total_oil * diesel_price

            # ======================
            # 结果展示
            # ======================

            st.markdown("## 📋 当前方案计算结果")

            c1, c2, c3 = st.columns(3)

            c1.metric("总施工台时", f"{total_hour:.2f}")
            c2.metric("预计工期（天）", f"{days:.2f}")
            c3.metric("总油耗（吨）", f"{total_oil:.2f}")

            c1, c2, c3 = st.columns(3)

            c1.metric("碳排放（tCO₂）", f"{carbon:.2f}")
            c2.metric("燃油成本（元）", f"{fuel_cost:,.0f}")
            c3.metric("影响系数", f"{factor}")

            # ======================
            # 优化推荐
            # ======================

            result = []

            for (ship, soil), unit in quota.items():

                if soil == soil_type:

                    hour = workload / 10000 * unit

                    ship_oil_rate = oil_rate[ship] / 1000

                    oil = hour * ship_oil_rate

                    co2 = oil * 3.114

                    cost = oil * 8500

                    days_ship = hour / 20

                    result.append(
                        [
                            ship,
                            hour,
                            days_ship,
                            oil,
                            co2,
                            cost
                        ]
                    )

            df = pd.DataFrame(
                result,
                columns=[
                    "船型",
                    "总台时",
                    "工期(天)",
                    "油耗",
                    "碳排放",
                    "成本"
                ]
            )
            # 满足工期要求的方案

            df_valid = df[
                df["工期(天)"] <= target_days
            ]

            # 如果没有满足工期要求的船型

            if len(df_valid) == 0:

                st.error("当前工期要求过于严格，无可行船型")

                st.stop()

            # ======================
            # 多目标优化
            # ======================

            if opt_mode == "最低碳排放":

                best = df_valid.loc[
                    df_valid["碳排放"].idxmin()
                ]

            elif opt_mode == "最短工期":

                best = df_valid.loc[
                    df_valid["工期(天)"].idxmin()
                ]

            else:

                # 归一化

                carbon_score = (
                    df_valid["碳排放"]
                    / df_valid["碳排放"].max()
                )   

                day_score = (
                    df_valid["工期(天)"] /
                    df_valid["工期(天)"].max()
                )

                cost_score = (
                    df_valid["成本"] /
                    df_valid["成本"].max()
                )

                df_valid["综合评分"] = (
                    carbon_score * 0.3 +
                    day_score * 0.5 +
                    cost_score * 0.2
                )

                best = df_valid.loc[df_valid["综合评分"].idxmin()]

            reduction_rate = max(
                0,
                (carbon - best["碳排放"]
                ) / carbon * 100
            )
            st.markdown("---")
            st.markdown("## 🤖 低碳优化推荐")

            st.success(
                f"""
            推荐船型：{best['船型']} m³/h

            预计碳排放：{best['碳排放']:.2f} tCO₂

            预计工期：{best['工期(天)']:.2f} 天

            预计减排率：{reduction_rate:.2f} %
            """
            )
        

            # ======================
            # 数据表
            # ======================

            st.markdown("## 📊 船型方案对比")

            st.dataframe(df, use_container_width=True)

            # ======================
            # 图1
            # ======================

            st.markdown("## 📈 不同船型碳排放对比")

            chart_df = df.set_index("船型")

            st.bar_chart(chart_df["碳排放"])

            # ======================
            # 图2
            # ======================

            st.markdown("## ⏳ 不同船型工期对比")

            chart_df = df.set_index("船型")

            st.bar_chart(chart_df["工期(天)"])

            # ======================
            # 图3
            # ======================

            st.markdown("## 💰 不同船型成本对比")

            chart_df = df.set_index("船型")

            st.bar_chart(chart_df["成本"])
            st.markdown("## 🏆 推荐方案排名")

            top3 = df_valid.sort_values(
                by="碳排放"
            ).head(3)

            st.dataframe(
                top3,
                use_container_width=True
            )
            st.dataframe(
                top3,
                use_container_width=True
            )

    if st.button("🏠 返回首页"):
        st.session_state.page = "home"
        st.rerun()
if st.session_state.page == "pro":

    st.title("✨ 碳智·浚浦（精装版）")

    st.markdown("---")

    # 工程基本信息

    st.markdown("## 📋 工程信息")

    c1, c2 = st.columns(2)

    with c1:
        project_name = st.text_input(
            "项目名称",
            "某航道疏浚工程"
        )

    with c2:
        project_place = st.text_input(
            "施工地点",
            "江苏省"
        )

    st.markdown("---")

    # 输入参数

    c1, c2 = st.columns(2)

    with c1:

        workload = st.number_input(
            "工程量（m³）",
            min_value=10000,
            value=100000,
            step=10000
        )

        st.info(
            "🤖 AI将自动推荐最优船型"
        )

    with c2:

        soil_type = st.selectbox(
            "土质类型",
            sorted(list(set([x[1] for x in quota.keys()])))
        )

        impact_level = st.selectbox(
            "客观影响等级",
            ["一级","二级","三级","四级","五级","六级","七级"]
        )

    if st.button("🚀 开始智能分析"):

        result = []

        for (ship, soil), unit in quota.items():

            if soil == soil_type:

                total_hour = workload / 10000 * unit

                days = total_hour / 20

                oil = total_hour * oil_rate[ship] / 1000

                carbon = oil * 3.114

                cost = oil * 8500

                result.append([
                    ship,
                    total_hour,
                    days,
                    oil,
                    carbon,
                    cost
                ])

        df = pd.DataFrame(
            result,
            columns=[
                "船型",
                "总台时",
                "工期(天)",
                "油耗",
                "碳排放",
                "成本"
            ]
        )
        carbon_score = (
            df["碳排放"] /
            df["碳排放"].max()
        )

        day_score = (
            df["工期(天)"] /
            df["工期(天)"].max()
        )

        cost_score = (
            df["成本"] /
            df["成本"].max()
        )

        df["综合评分"] = (
            carbon_score * 0.4 +
            day_score * 0.4 +
            cost_score * 0.2
        )
        best = df.loc[
            df["综合评分"].idxmin()
        ]
        st.markdown("---")

        st.markdown("## 🧠 AI决策解释")

        best_carbon = df["碳排放"].min()
        best_day = df["工期(天)"].min()

        carbon_improve = (
            (df["碳排放"].max() - best["碳排放"])
            / df["碳排放"].max()
            * 100
        )

        day_improve = (
            (df["工期(天)"].max() - best["工期(天)"])
            / df["工期(天)"].max()
            * 100
        )

        st.success(
            f"""
        🤖 AI综合分析结果

        推荐采用 {best["船型"]} m³/h 船型。

        相比同类方案：

        ✅ 工期缩短 {day_improve:.1f} %

        ✅ 碳排放降低 {carbon_improve:.1f} %

        ✅ 综合评分排名第一

        该方案兼顾施工效率、
        经济成本与低碳目标，
        建议优先采用。
        """
        )

        st.markdown("## 🤖 AI智能决策报告")

        st.success(
            f"""
        🏆 AI推荐船型：{best['船型']} m³/h

        预计工期：{best['工期(天)']:.2f} 天

        预计碳排放：{best['碳排放']:.2f} tCO₂

        预计成本：{best['成本']:,.0f} 元
        """
        )
        worst = df.loc[
            df["碳排放"].idxmax()
        ]

        reduce_carbon = (
            worst["碳排放"]
            - best["碳排放"]
        )

        reduce_rate = (
            reduce_carbon
            / worst["碳排放"]
            * 100
        )
        st.markdown("## 🌱 AI减排潜力分析")

        st.info(
            f"""
        如果采用AI推荐方案：

        预计减少碳排放

        {reduce_carbon:.2f} tCO₂

        减排率

        {reduce_rate:.2f} %
        """
        )
        st.markdown("## 🏆 全船型排行榜")

        rank_df = df.sort_values(
            by="综合评分"
        )

        st.dataframe(
            rank_df,
            use_container_width=True
        )

        st.markdown("## ⚠ 风险预警")

        if best["工期(天)"] > 30:

            st.warning(
                "施工周期较长，存在延期风险。"
            )

        elif best["碳排放"] > 300:

            st.warning(
                "碳排放水平较高，建议进一步优化。"
            )

        else:

            st.success(
                "当前方案风险较低，可实施性较好。"
            )

        st.markdown("## 🌳 低碳效益评估")
        worst_carbon = df["碳排放"].max()

        carbon_saved = (
            worst_carbon -
            best["碳排放"]
        )

        tree_num = carbon_saved / 0.0183

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "减排量",
                f"{carbon_saved:.2f} tCO₂"
            )

        with c2:

            st.metric(
                "折算植树量",
                f"{int(tree_num)} 棵"
            )

    if st.button("🏠 返回首页"):
        st.session_state.page = "home"
        st.rerun()