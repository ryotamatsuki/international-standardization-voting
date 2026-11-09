# 実証可能性・制度的正確性の監査（命題選定段階）
Date: 2026-11-09. **公開の実データ・スキーマや制度の存在を確認した段階。個票を取り出して因果推定したわけではない。**

## A. 第一候補が必要とする識別変数
**政策露出**：協定A–Bの発効・特定セクター・適合評価scope・対象指定CABの差分。
**別市場Dの法的有効性**：BにあるCABがD国向けに指定されている、またはD国がそのscopeで当該CABの証明を直接認める。**A–B–Dの相互承認の自動推移を決して仮定しない。**
**第三国企業Cの合法的なCABアクセス**：C企業がBのCABに試験を委託できるか、製造国に関する制限があるか、必要な検査・評価内容がDの要求と一致するか。
**CAB供給反応**：指定対象scopeの設備投資、認定試験分野、試験料金、予約待ち、認定から実サービス提供までの時差。**この変数が全く観測できないとC1の核を直接検証できない**。
**市場成果**：C→Dのセクター別新規輸出者数・新規品目・平均参入コスト/期間。輸出額のみなら非締約国の再配分と混同する。

## B. 公開ソースと到達範囲（具体的リンク）
1. **OECD Trade Policy Paper 307（2026-11-05）** https://doi.org/10.1787/56f2cfc7-en 。112件のMRA/MLA/CAB arrangementsを2024年時点で分類（2026年報告）。先行研究に基づき協定の貿易効果、認証実装の弱点、第三国の間接効果の未解明を報告。**文献・集計表は公開閲覧可能**。研究用の112件全個票CSVの外部ダウンロード可否は**未確認**；公開報告書を読み、存在しないCSVを仮定しない。
2. **EU公式の対外MRA** https://single-market-economy.ec.europa.eu/single-market/goods/international-aspects/mutual-recognition-agreements_en 。各協定および指定されたCABの正式リスト。EU–Japan等の国別協定にCAB scope・適用部門がある。A/Bの具体的MRAとDへの別の認定範囲を合わせて確認する必要。
3. **欧州認定機関 EA** https://european-accreditation.org/sp_accordion_faqs/is-there-a-database-with-all-accredited-laboratory-inspection-certification-verification-bodies-and-their-accredited-scopes/ 。**CABの全世界/全欧統合名簿は無い**と公式に説明。各国家認定機関のscope別ディレクトリを辿る。データ統合は実質的な作業。
4. **スイス SECO MRA解説** https://www.seco.admin.ch/en/general-information-mra ：通常MRA（輸入国の技術要件を満たすことを外国CABで検査）と拡張MRA（技術要求自体が相当）の違いが明確。
5. **シンガポール認定機関** https://www.sac-accreditation.gov.sg/about/collaborations-and-recognitions/mutual-recognition-arrangement/ ：認定分野と国際的受入ネットワークが重要（2026年8月更新）。公式制度例として使用可能だが個票のCAB試験金額や利用者国は公開確認していない。
6. **ISO Open Data** https://www.iso.org/open-data.html ：国際規格発行日・改訂情報・ICS・技術委員会・参加国のメタデータはCSV等で公開。**個別案件の国別投票や企業の実装、CAB料金、輸出者個票は含まない**。
7. **WTO TBT／ePing** https://www.wto.org/english/tratop_e/tbt_e/conformity_assessment_proc_e.htm ; https://data.wto.org/en/dataset/ext_eping ：規制変更と適合性評価の通報。**MRIに基づく各企業の適合証明の利用件数ではない**。
8. **UN Comtrade** https://comtradeapi.un.org/ ：貿易品目の集計。ICS/ISOの技術セクターや認定scope→HS分類には多対多対応が多く、機械的1対1照合をしてはいけない。
9. **World Bank WDR2025** https://www.worldbank.org/en/publication/wdr2025 ：国内認証能力の格差、低所得国の市場アクセス。補助的な制度的背景に適する。
10. **UK GOV.UK** https://www.gov.uk/guidance/conformity-assessment-testing-under-mutual-recognition-or-free-trade-agreements ：英国が相互承認対象の指定CABで輸出先市場要件を試験できる条件を説明。**「CABの所在国」＝「商品の製造原産国」という推論は誤り**。

## C. 研究対象の実データ実現性（机上確認）
- **実施可能性の高い最初のケース候補**：EUの複数のMRA締約国CAB／対象製品（電子・電気機器等）から、輸出先Dで受入れ済みのCAB資格を持つB国の機関を1件選び、第三国Cにサービスを販売した事実を確認。**対象機関は未特定**のためこれは調査計画であり、事例の発見を装わない。
- **ネットワークのグラフ**：ノードは各国/機関、エッジは**scopeと期間で限定された法的な証明受入れ関係**とし、締結のニュースをそのまま有効エッジにしない。指定CABの有効期限/停止/相互承認の範囲を記録する。
- **第三国企業の利用**：第三国へのサービス提供が許容されても、実際の委託件数の公表は不明。**観測不能ならC1を直接検証不能と記録**。
- **輸出者個票・料金**：UN Comtradeだけでは企業別の市場参入は測れない。国別通関マイクロデータ・CAB試験記録または機関共同研究が必要かもしれない。まず公開業界認定一覧・公表料金・納期で代理変数の実現可能性を確認する。
- **対照群**：A–B協定が対象とする認定試験scopeと、同一B国CABの非対象scopeの対照。ただし内生的協定選択・並行政策/市場需要・認定scopeの異なる景気動向を警戒。
- **因果推論**：協定発効前後のDiDを自動提案しない。政策の内生性と事前趋势を評価。適合性評価の受入の実施日・CAB指定日・実際のサービス開始日は別。
- **反証**：B CABの料金/待ち時間/設備能力に変化がなく、C→D新規参入もB–D事前受入に無関係ならC1の構造は支持されない。

## D. 他の二候補の観測可能性
**C2：** MRI発効日・CAB指定日、技術規格の変更/整合日、企業製品認証日が取得できれば制度順序を調べられる。投資が事前に織り込まれる問題がある。2026 OECD報告に実務の通関システムとの接続欠落がある。
**C3：** 技術規格の必須core、optional profile、上位profileの公的な定義と製品別取得履歴、次の認定への移行率が必要。OCAがOCPPの認証profileを公開している（ただしOCAはISO国別投票機関ではない）; profileを経済的な能力tierと等置しない。

## E. データゲート（研究に進む条件）
[C1 gate 1] 実際のA–B MRIを一つ選び、その後のB CABのscopeとD国による受入れを**公的文書で**示す。
[C1 gate 2] 非締約国Cの企業がB CABを使ってDへ輸出する経路が法的に有効か明示する。
[C1 gate 3] B CABの能力または料金の「前後」を示せるデータを一つ確保する。
[C1 gate 4] C→Dの新規参入またはテスト利用という成果指標を実際に観測できることを確認する。
この4つに到達するまでは**実証可能性を「概念上あり、データ入手未確認」**と表現し、因果識別の達成を主張しない。
