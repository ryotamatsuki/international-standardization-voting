# 国際標準化の均衡理論：先行研究に対する実質的新規性の独立敵対的査読報告書

**作成日：**2026-11-08  
**対象：**`ryotamatsuki/international-standardization-voting`  
**読取時の研究ブランチHEAD：**`b50f6596c36689f97a6b7a9f8fb40f7cfae67d6f`（`research/p1-proof-novelty-gate-20261108`）  
**main比較元：**`8feb4a242eaa7cb8c186a7e0f82fe76ba003cb02`（当時32コミット先行、19変更ファイル）  
**種類：**公開資料・原著・数式・再現コードに基づく独立模擬査読。実在する匿名査読、掲載判断または独創性の法的保証ではない。

## I. Executive Editorial Decision
**結論：未確定（現状で「実質的に新しい独立均衡メカニズム」を確認できず）。現行P1は研究結果として保持するが、IJIOへの現状投稿は見送る。**

中心結果の価格ゲームの均衡存在、企業採用の条件付き厳密な継続均衡、人口比率が自由な国別支持閾値と世界厚生の検証は評価できる。一方、「既存互換ネットワーク企業は互換化による相対優位の喪失を嫌う」「投票ルールで福祉改善を拒否する」という経済的誘因と制度的結果は先行研究で広く知られる。中核の3/4投票の `median` 閾値は単交差利得を投票規則へ入力した順序統計である。新規の**閾値値**と新規の**経済メカニズム**を混同しない。完全同型が判明したGate 4技術反対票ゲーム（Volunteer’s Dilemma）は主定理にならない。Gate5Aの供給モデルは説明上の改善だが、事前の規格承認によって新たな外部需要Rが生じる点は仮定。

投稿適合性（主観的編集判断）：IJIO未到達、RIOは新しい制度・提案均衡が実証されれば検討、Journal of EconomicsはP1の短い理論論文の候補になり得るが、**同誌2025年掲載Cheng & Huang**と2023年Buccella等の重複を明確に処理した後のみ判断できる。確率の根拠ある推定はしない。

## II. 4原著の再構成と証拠等級
### Gandal & Shy 2001, JIE 53:363–383【公刊全文、ユーザー提供PDF】
§2：3市場3企業、長さ3のSalop円環。消費者効用はブランド総価値V_i^k、地域別価格、距離の二乗による負効用。ブランド互換数による利得d、外国規格の不承認時は転換費用c。§2.3で政府の基準承認→地域別企業Bertrand価格→需要、後ろ向き帰納。政府目的は地元CS+自国企業の世界利潤（§2.6 Eq(10),(11)）。§3 Proposition 1：転換費用の内点領域で全面外国規格承認が支配戦略。Propositions 2–3：排他的二国連合が国内の輸出者利潤増加によって利益となり得る。§3.3：国別人口非対称性を既に検討。§4 Proposition 4：純粋なネットワーク外部性の全面承認は支配戦略。Proposition 5及び§4.2.2：排他的連合より全面相互承認が選好される。
**注意**：§4のall/none承認では全ブランドに同等の品質増分が生じ価格・利潤は変わらない。P1の3対1既存ネットワーク→全面互換では**相対品質が変化して利潤が移転する**。よって一方が他方の言い換えとは言えないが、§3.2の排他的連合の競争優位移転という経済誘因は重複する。

### Barrett & Yang 2001, JIE 54:171–191【公刊抄録、1999年改訂WP全文】
1999年改訂版（https://ageconsearch.umn.edu/record/14597/files/wp9909.pdf）で少なくともProposition 1（国内旧技術の既存加入基盤と旧技術側への互換化による市場拡大）、Proposition 3（旧国内技術との完全一致・事前基盤不在を除いて国際規格より旧技術側への適合が利潤上有利）、Proposition 7（成熟ネットワークでは消費者便益重視の政府が旧規格への適合を選好）を確認。さらに同WPでは政治経済的投票による政策も議論。国内に既存規格を持つ主体の合理的非互換、および政府による支持は**確実に既知**。ただしこの1999年版の命題番号・文面を2001年公刊版へ無断で同一視しない。

### Klimenko 2009, JIE 77:151–166【公刊抄録・序論のみ】
国内・外国製品間の技術互換性、政府間戦略的規制、完全競争と国際複占、ネットワーク強度に依存する過度の互換化または互換不足を分析。公刊全文の特定命題と証明は今回入手できず、P1比較静学の形式的包含は**未判定**。これを「Klimenkoには無い」と解釈してはならない。 https://doi.org/10.1016/j.jinteco.2008.08.005

### Spulber 2019, Economic Journal 129:1477–1509【公刊全文HTML】
公刊版（https://onlinelibrary.wiley.com/doi/10.1111/ecoj.12606）の**Proposition 6**はSEPのない垂直関連採用者群で多数決により効率的規格を選ぶ条件、**Corollary 2**は効率的技術革新品質が上昇すると支持票数が減少しないこと。P1の横方向ブランド競争・輸出者利潤帰属・国内票と異なるため反例ではない。また革新品質と互換ブランド便益強度dは同じパラメータでない。2016年WPと命題番号が異なるため公刊版を優先。

## III. 数学的・戦略的関係の分類
1. Gandal–Shy：対象の3+1→4品質差分と認知選択の相対利潤効果が違い**厳密同型未証明**、ただし世界利潤帰属・排他的利益は既知。標準化連合への追加的制度応用：**3〜4**（新理論メカニズム5ではない）。
2. Barrett–Yang：国際規格から既存規格の利益を守る合理的非互換という方向は重複。P1の4票集計は当該1999年WP主要命題から直接導出される形は確認できず：**3〜4、ただし最終刊行版監査必要**。
3. Klimenko：国家の互換性政策・ネットワーク強度の比較静学の近接性は高く、定理の形式的重複：**6判定不能**。
4. Spulber：同じ投票＋市場競争でも投票者、利得原始条件、技術改善変数が異なる：**直接包含なし。ただし一般的な投票非効率の新規性は3以下**。
5. Gate4対DiekmannのVolunteer's Dilemma：**2数学的同値**。各プレイヤーの利得へ定数L_iを加えるだけで完全に同一のゲームを得る。
6. 追加：Cheng & Huang, *Journal of Economics* 145 (2025): 31–57, DOI 10.1007/s00712-024-00896-5：企業の互換化に拒否権がある場合、強いネットワーク外部性が非互換を生む。**方向性の重複リスク大**、公刊全文はアクセス不可で形式的包含は不明。
7. 追加：Buccella, Fanti & Gori 2023 *Journal of Economics* 140:141–168、DOI 10.1007/s00712-023-00834-x：互換化の企業選択を非協力ゲームとし多重SPNEを分析、全文確認。Gate2の自発採用だけで新規性は立たない。
8. 追加：Buccella, Fanti & Gori 2026 issue (online 2025), DOI 10.1080/10438599.2025.2478583：**BertrandとCournot**の互換化選択と変動費用、複数SPNEを分析、採用段階の近接研究。
9. 追加：Delaney & Driouchi, *Economic Theory* (2025), 'Coordination through Committees and Markets with Option Timing Games', DOI 10.1007/s00199-025-01654-4：委員会と市場における規格調整・既得権と合意、2025年の近接理論。完全定理対照は未実施。
10. Fu, Tan & Wang 2023 *IJIO* 88:102952：競合SSOによる技術選択、ネットワーク効果、連合形成。内生的標準範囲P2を提案する際の直接比較対象。

## IV. P1の形式再構成
4国家4企業の連続価格競争にて旧品質 `(2d,2d,2d,0)`、新品質 `(3d,3d,3d,3d)`。閉形式価格は `(1+d/3,1+d/6,1+d/3,1-5d/6)` 対 `(1,1,1,1)`。価格ゲームの一方向逸脱を排除する十分条件は原著リポジトリのGate1証明内で `0<d<6/7`。価格Nash均衡の**存在**であって唯一性ではない。16継続状態を含む検査は一段強いが依然全てのSPEの一意性ではない。
世界消費者余剰と利潤の検査：
`ΔCS_circle=d(216-13d)/36`;
`Δπ_circle=(-d(d+6)/9,-d(d+12)/36,-d(d+6)/9,d(60-25d)/36)`。
`ΔW_i=N/4 [w_i ΔCS_circle+Δπ_i_circle]`、企業3所在国では実装費`k_L`控除。周辺既存国の賛成閾値 `w_i>=4(d+6)/(216-13d)`、中央既存国は `w_1>=(d+12)/(216-13d)`。人口は特定の比率へ固定しない。国家3は `k_L<G_3=Nd(60-25d)/144<k_H` なら確実に賛成。中央を含めた既存3社の個別臨界値の**中央値**が3/4採決の臨界値。3/4ルールと単交差の既知の機械的結合。
ネット社会厚生増分は `Nd(216-47d)/144-k_L` で、投票否決後の厚生損失が成立し得る。これは実装が可決後の継続均衡で生じるときの**条件付き厚生**である。
原始条件は「相互互換する追加**ブランド数**×d」。利用者全体のネットワーク規模でない。
業界利益の重み `β_i/α_i` と国家国内市場規模 `w_i` は投票に影響するが、国内市場の重み・世界利潤帰属という利得構造自体は基準論文と同系統。

## V. 反事実モデル（必要条件の切り分け）
- 投票規則だけを2/4、3/4、4/4へ変更（全有効票）すると、企業3賛成の下で既存三社の臨界値の**最大値／中央値／最小値**がそれぞれ採決臨界値。元の国0・2同じ規模例では3/4と全会一致が同時に否決へ切り替わり、ISO特別多数決の不可欠性は示されない。
- 原稿の非対称人口(0.12,0.42,0.13,0.33)、k_L=.05、k_H=.3、d=.2,.4,.8：票は4→3→2。2/4は最後まで承認、3/4は最後に否決、4/4は中間から否決。条件付き世界厚生はそれぞれ853/3600,112/225,847/900で正。独立SymPy再計算済。
- 「承認→互換、否決→3+1」を企業採用選択ではなく**外生**と定めると、投票閾値と厚生式は完全に再現。**投票反転の数学には任意採用ステージ不要**。ただし逐次ゲームの経済的解釈では重要。
- 企業世界利潤の国別重みを0にすると全既存国は改善を支持して反転が消える。利潤の国内帰属は当該モデルの必要メカニズムだが既知。
- 国内人口を全て1/4に等しくし国の社会厚生重み`α=β=1`を維持すると本証明領域に反転なし。国内利益集約で`β/α=2`なら対称人口でも反転し得るが、**利得原始条件を別に変更した結果**として扱う。
- 実際のISO二重閾値ではYes2/No0/Abstain2は承認、Yes2/No1/Abstain1は否決。経済的不利益だけで有効技術反対票を作れるとは限らない。
- ISO発行が技術的利用可能性、開発費、補完財需要、期待、均衡選択を全く変えないなら、否決と可決後のゲームは同型であり、承認に因果的普及効果は認められない。
- ブランド数効果をユーザーの導入ベース効果へ変えたときの比較静学は未導出。
- 国別実装ツールの供給を扱うGate5Aは`G<F<G+R,K>G`の契約可能領域で普及を説明するものの、承認で生じる第三者需要Rの存在は依然仮定。

## VI. H0-A〜H0-Gの敵対的判定
| 帰無仮説 | 判定 | 主たる理由 |
|---|---|---|
| H0-A P1=G&SのSU均衡の単なる改称 | 完全同一は否定的、類似誘因は確認 | §4全員への共通品質便益とP1競争上の品質非対称性は異なる一方、世界利潤・連合形成誘因は既知 |
| H0-B =Barrett–Yang合理的非互換 | 経済メカニズムでは強く支持、形式同値未確認 | 既存規格と国際標準の対立、政府誘因既知 |
| H0-C Klimenkoから直接導出 | 未確定 | 公刊全文・命題番号未確認 |
| H0-D Spulberへ利得投入 | 単なる定理代入としては不成立、一般原理は既知 | 垂直関連採用者と横方向の国家輸出者帰属の原始条件が異なる |
| H0-E 適当な単交差国別利得で同一の投票反転を作れる | **支持** | 各国の符号と3票閾値の順序統計にすぎない（価格競争は利得微視的基礎を与えるだけ） |
| H0-F 採用内生化がなくても反転する | **支持（投票数式について）** | 結果条件付きで可決/否決の採用状態を固定すれば厳密に同式。ただし現実の普及説明は失われる |
| H0-G ISO固有でなく3/4なら何でも | **支持（P1の基幹命題について）** | ISO固有の実質的技術コメント適格性・棄権が主命題に入っていない |

## VII. 中心命題の限定的英語再定式化（新規性を主張する声明ではない）
**Proposition (Conditional Network-Intensity Reversal of International Approval).** Consider four segmented Salop–Bertrand markets and four nationally owned firms, three of which initially supply mutually compatible products. Suppose the post-ballot standard-adoption game has selected strict continuation Nash equilibria under which publication induces the fourth firm to adopt compatibility, while rejection preserves the initial three-plus-one configuration; suppose the price equilibria satisfy the stated global unilateral-deviation conditions, and national delegates cast sincere votes with indifference resolved in favour of approval. For any positive national market shares summing to one, incumbent national support is characterized by the country-specific thresholds specified in §IV, and the published-standard proposal passes a three-of-four ballot if and only if network intensity does not exceed the median of the three incumbent critical values. There exist nonempty open parameter regions in which increased network intensity changes the proposal's outcome from approval to rejection despite a strictly positive world welfare gain conditional on implementation.
**Assumptions.** Positive but asymmetric national product demand; common quadratic Salop transport cost; brand-count interoperability bonus; nationally appropriated worldwide profits; fixed national approval weights; specified adoption continuation selection and publication-dependent incentive primitive; 4 valid ballots; 0<d<6/7 and compatible implementation resource costs within the open private adoption interval.
**Economic interpretation.** Global incumbent-profit losses can outweigh local consumption gains in small-market exporter countries. Equal national ballot rights aggregate these losses discretely and can block a welfare-improving standard. **Novelty caveat:** Neither anti-compatibility exporter incentives nor simple majority aggregation is new in itself. This proposition is mathematically conditional; originality remains unsettled.

## VIII. 投稿先別編集判断
**IJIO:** 現行P1だけで送付非推奨。既知の標準化投票、企業の非互換誘因、世界利潤帰属からの簡単な合成であるとの指摘が最大リスク。関連実績：Fu–Tan–Wang (2023) *Policy orientations and technology choices in standards wars*, Llanes (2024) *Innovation incentives in technical standards*, 2026 IEEE特許政策研究。それぞれ標準化機構と市場で新しい因果的反応を示す。P1は新たな制度相互作用定理が必要。
**Review of Industrial Organization:** 条件付き。2025年の理論掲載例Emons–Lenhard *The Economics of Advice*は小規模モデルも扱うが、明快な独立メカニズムがある。既知ゲームへの代入だけでは説得力不足。市場競争と実際のISO制約が均衡を変える命題を証明する。
**Journal of Economics:** 最も近い現実的な検討先。ただし同誌の**Buccella–Fanti–Gori (2023)**と**Cheng–Huang (2025)**は企業互換性の内生化や強いネットワーク外部性による非互換を既に扱うため、これらを論文中で具体的に対照しない限り重大な重複リスク。現状のまま投稿は勧めない。
掲載確率を数値で見積もるための受理率や編集者行動データはなく、確率を提示しない。

## IX. 最少の次研究計画
1. **まず原著全文に基づくGate-N（負の新規性検定）**：Cheng & Huang (2025)、Barrett & Yang (2001)の最終版、Klimenko (2009)の定理番号と証明を入手。利用可能な原始条件から戦略形同値性・比較静学の写像を調べる。確認不能な文献を理由に新規認定しない。
2. **内生的な国際規格案と実装投資・投票の相互作用**：提案者が互換性範囲と技術的仕様を変えられ、反対票の技術的根拠と後続投資が反応する逐次均衡を最小状態で導出する。既知の投票閾値と製品市場利益を入れるだけでは発生しない独立の帰結を必要条件・十分条件で証明。Farrell–Simcoe、Fu–Tan–Wang、Delaney–Driouchiと比較。
3. **成功した場合だけ一般性の検証**：実際の利用者基盤に比例するネットワーク便益、分割所有/人口・世界市場比、n国の票数、均衡選択への頑健性を必要最小限で検証。多数の拡張や新たな閉形式を増やすこと自体を目標にしない。

## 検証状況と残余不確実性
本報告は**一般的な全ての先行研究の不存在証明ではない**。公刊全文を閲覧できたのはGandal–Shy（ユーザー提供）、Spulber（オンライン全文）、Buccella等(2023)等。Barrett–Yangは1999年改訂版全文、KlimenkoとCheng–Huangは公刊抄録が中心。著者原稿と公刊版の定理番号混同は回避。実装費等が投票によって変わる仮定には制度的根拠上の限界あり。

## 関連する同ブランチ追加検証
- `literature/independent_adversarial_novelty_audit_20261108.md`：論文別命題・証拠基準・H0検証
- `proofs/independent_counterfactual_equivalence_20261108.md`：解析的反事実・戦略形の関係
- `code/test_independent_novelty_counterfactuals_20261108.py`：SymPy厳密有理数検証
既存のGate1、Gate2、Gate4、Gate5Aの原本・コードは変更しない。
