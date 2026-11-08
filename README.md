# International Standardization Voting

> **2026-11-08 Proof & Novelty Gate — 検証更新（レビュー用ブランチ）**
>
> - [Gate 1：閉形式の大域的Bertrand均衡証明](proofs/gate1_closed_form_global_bertrand.md)：候補均衡価格の一方的逸脱を排除。指定モデルの (0<d<6/7) で成立。
> - [Gate 2：企業の任意採用と投票の部分ゲーム](proofs/gate2_voluntary_adoption_equilibria.md)：公開による実装費低下の仮定下で、投票帰結に対応する厳密な継続Nash均衡の存在。
> - [ISO制度・国内利害集約・新規性の独立監査](literature/p1_institutional_validity_prior_art_audit_20261108.md)：国家標準化機関の選好と、有効な反対票を区別。FDISの技術的反対理由と承認後実装費用仮定が主要な未解決点。対称人口でも産業利益の重みで反転する頑健性結果を検証。
> - [人口比率の一般化：Median-pivot theorem](proofs/p1_population_generalization.md)：人口比率を固定せず、国別の賛成閾値と採択閾値を閉形式で導出。異なる人口比率でも4→3→2票となることを証明。
> - [Gate 3：先行研究との敵対的比較](literature/gate3_novelty_audit.md)：Spulberの定理と形式的に異なるが、新規性の独立性は未確定。
> - [統合判定と検証記録](research_log/2026-11-08_gate123_results.md) / [正確な有理数を使った検証コード](code/test_gate123_closed_form.py)
>
> **要点**：数学的な均衡存在の証明は進展。一方、ISO固有の制度効果と先行研究に対する新規性には引き続き大きな課題がある。


**国際標準の意思決定とネットワーク外部性：研究リポジトリ**

基準論文：Gandal & Shy (2001), [*Standardization Policy and International Trade*](https://doi.org/10.1016/S0022-1996(00)00067-2), *Journal of International Economics*.

研究状態（2026-11-08）：**予備理論研究・独立検証段階。未投稿。新規性と掲載可能性は未確定。**

## 収録内容

| 保存先 | 内容 |
|---|---|
| [標準化研究の歴史（日本語）](literature/history_1985_2026_ja.md) | 1980年代のネットワーク外部性・互換性から2026年の研究まで、直接系譜と関連研究を区別したレビュー |
| [文献・新規性照合表](literature/bibliography_and_novelty.md) | 主要文献のモデル、既知結果、本研究への重複リスクと参照リンク |
| [理論モデルと仮説](theory/model_and_hypotheses.md) | P1・P1-A・P2・P3、H1〜H10の数式、定義、未検証項目 |
| [P1条件付き証明ノート](proofs/p1_conditional_adoption.md) | 投票反転と企業の自発的互換化を結びつける成立条件、限界 |
| [P1の基礎検証コード](code/p1_iso_verification.py) | SymPyによる価格・厚生・閾値の代数検査と価格逸脱のサンプル検査 |
| [P1の採用検証コード](code/p1_iso_endogenous_adoption.py) | ISO承認後・非承認後の私的採用誘因、投票・世界厚生の再現 |
| [初期研究ログ](research_log/2026-11-08_initial_assessment.md) | 予備研究の到達点、Cournotモデルの未再現部分、投稿先別評価、次のゲート |

## 主たる結果（P1）

4か国Salop型Bertrand競争。企業0・1・2の既存互換ネットワークと、孤立した企業3の完全互換化を比較。ISO型の最終投票は、4 Pメンバー全員が有効賛否票を投じる場合、3票賛成で可決する。

国内市場人口の比率が (0.12, 0.50, 0.12, 0.26) の例では、国0と国2の厚生差が

\[
\Delta W_0=\Delta W_2=\frac{Nd(48-139d)}{3600}
\]

となり、ネットワーク強度 \(d^* = 48/139\) で賛成から反対へ反転する。反転の前後で、全面互換化は世界厚生を改善する。

**P1-A（承認と任意採用）：** 規格が発行されることで企業3の実装費用が \(k_H\) から \(k_L\) に下がると**仮定**し、企業3の私的追加利潤 \(G_3(d) = Nd(60-25d)/144\) が \(k_L<G_3(d)<k_H\) を満たすと、承認後は自発的に採用、非承認後は不採用となる。承認が実装費用を下げる効果自体はモデルから証明していない。

## 研究上の未解決点

1. P1の価格均衡が、反転閾値の前後の区間で**あらゆる価格逸脱に対して**Nash均衡であることを、査読可能な形で証明する。
2. 既存企業による規格の維持と、企業3による実装の意思決定を一貫して定義し、可決・否決のサブゲームを解く。
3. [Spulber (2019)](https://doi.org/10.1111/ecoj.12606)、[Barrett & Yang (2001)](https://doi.org/10.1016/S0022-1996(00)00082-9)、[Klimenko (2009)](https://doi.org/10.1016/j.jinteco.2008.08.005) と定理レベルで重複を確認する。
4. これらが通過して初めて、P2（互換性水準の内生的な提案・修正）を追加する。

## 再現方法

PythonとSymPyが必要。

~~~bash
python -m pip install -r requirements.txt
python code/p1_iso_verification.py
python code/p1_iso_endogenous_adoption.py
~~~

コードの PASS は、数式的整合性や有限のテスト点の通過を意味する。連続戦略空間に対する機械的な形式証明ではない。

## 投稿誌の暫定評価

- **IJIO:** 未到達。一般的な新メカニズムと既存定理との差分が必要。
- **Review of Industrial Organization:** 追加的な命題・堅牢な均衡証明が成立すれば候補。
- **Journal of Economics 等の関連専門誌:** 完成した最小理論として成立する可能性を評価中。

これらは掲載確率の保証ではない。

## ISO制度との違い

ここで採用したのはISOの **DIS/FDIS最終投票の簡略化**であり、ISO全体の実際のプロセス（NP承認・専門家派遣・CDコンセンサス形成・技術的な反対コメント・否決後の差戻し）を完全に表現するものではない。ISOの規格発行は市場での採用の強制ではない。

[ISO/IEC Directives Part 1 (2026)](https://www.iso.org/sites/directives/current/consolidated/) を制度上の一次資料とする。

研究内容を公開する際は、未投稿の独自結果であることと新規性未検証の事実に留意すること。出版者のPDFは本リポジトリに再配布しない。
