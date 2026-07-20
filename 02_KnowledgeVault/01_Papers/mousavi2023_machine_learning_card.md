---
title: "Machine Learning in Earthquake Seismology"
authors: [Mousavi, Beroza]
year: 2023
venue: "Annual Review of Earth and Planetary Sciences"
task: [Seismic Event Monitoring, Earthquake Seismology]
method: [ML, Deep Learning, CNN, RNN, Transformer, GAN, PINN]
dataset: [NCEDC, various]
code_available: Mixed
importance: high
reading_status: done
tags: [survey, ml, earthquake-seismology, annual-review, mousavi-beroza]
created: 2026-07-09
---

# Basic Information / 鍩烘湰淇℃伅

- **Title**: Machine Learning in Earthquake Seismology
- **Authors**: S. Mostafa Mousavi (Google) and Gregory C. Beroza (Stanford)
- **Year**: 2023
- **Venue**: Annual Review of Earth and Planetary Sciences, Vol. 51, pp. 105-129
- **Task**: Comprehensive survey of ML applications in earthquake seismology
- **Method**: Survey 鈥?reviews event discrimination, detection, phase picking, location, magnitude, source parameterization, seismogram simulation, ground motion
- **Dataset**: Multiple (NCEDC, Japan Tottori, Italy Amatrice-Visso-Norcia, etc.)
- **Code**: Mixed (various open-source tools cited)

# Research Problem / 鐮旂┒闂

> 绯荤粺缁艰堪鏈哄櫒瀛︿範鍦ㄥ湴闇囧涓殑搴旂敤杩涘睍锛屾兜鐩栦粠浜嬩欢鍒ゅ埆鍒版尝褰㈡ā鎷熺殑8澶т换鍔★紝骞舵寚鍑烘湭鏉ユ柟鍚戙€?
# Main Contribution / 涓昏璐＄尞

> Annual Review绾у埆鐨勫叏闈㈢患杩般€傛寜鍦伴渿澶勭悊浠诲姟锛堝垽鍒啋妫€娴嬧啋鎷炬尝鈫掑畾浣嶁啋闇囩骇鈫掓簮鍙傛暟鈫掓ā鎷熲啋鍦拌〃杩愬姩锛夌粍缁囨枃鐚紝鎻愪緵浠庝紶缁烝I鍒版繁搴﹀涔犵殑婕旇繘鑴夌粶锛屾寚鍑哄熀鍑嗘暟鎹泦鍜屽紑婧愭鏋剁殑缂哄け銆?
# Method Overview / 鏂规硶姒傝堪

> 缁艰堪鎬ц鏂囷紝鎸変换鍔″垎绫荤粍缁囷細2.1浜嬩欢鍒ゅ埆銆?.2淇″彿妫€娴嬨€?.3闇囩浉鎷炬尝銆?.4瀹氫綅銆?.5闇囩骇浼拌銆?.6婧愬弬鏁板弽婕斻€?.7娉㈠舰妯℃嫙銆?.8鍦拌〃杩愬姩琛ㄥ緛銆傛瘡鑺傚洖椤炬棭鏈烝I宸ヤ綔鈫掓繁搴﹀涔犵獊鐮粹啋褰撳墠SOTA鈫掑紑鏀炬寫鎴樸€?
# Dataset and Evaluation / 鏁版嵁闆嗕笌璇勪及

- 缁艰堪娑电洊澶氫釜鏁版嵁闆嗭細NCEDC鍖楀姞宸炪€佹棩鏈笩鍙栥€佹剰澶у埄闃块┈鐗归噷鍒囥€佹櫤鍒╀刊鍐插甫绛?- 璇勪及鏂规硶鍥犱换鍔¤€屽紓锛氬垎绫诲噯纭巼锛堝垽鍒級銆丳recision/Recall/F1锛堟娴?鎷炬尝锛夈€佹畫宸紙瀹氫綅/闇囩骇锛?- 璁烘枃鎸囧嚭缂轰箯缁熶竴鍩哄噯鏁版嵁闆嗘槸棰嗗煙鍙戝睍鐨勭摱棰?
# Why This Paper Matters / 涓轰粈涔堝叧娉ㄨ繖绡囪鏂?
> Annual Review鏄鍩熷唴鏈€鍏峰奖鍝嶅姏鐨勭患杩版湡鍒婁箣涓€銆備綔鑰匨ousavi鏄疎QTransformer锛堝湴闇嘥ransformer锛夌殑浣滆€咃紝Beroza鏄疨haseNet鐨勫甯堛€傝繖绡囩患杩颁唬琛ㄤ簡Stanford瀛︽淳瀵硅棰嗗煙鏈€鏉冨▉鐨勬€荤粨銆傚叾鎸囧嚭鐨?鍩哄噯鏁版嵁闆嗙己澶?鍜?寮€婧愭鏋?寤鸿鐩存帴鎺ㄥ姩浜哠eisBench绛夊伐鍏风殑鍙戝睍銆?
# Limitations / 灞€闄愭€?
> 缁艰堪鎬ц川锛屼笉鎻愬嚭鏂版柟娉曘€傞儴鍒嗗瓙棰嗗煙锛堝鐏北鍦伴渿銆佹簮鏈哄埗鍙嶆紨锛夎繘灞曡緝鎱紝鏂囩尞鐩稿鏈夐檺銆傛繁搴﹀涔犲湪闇囨簮鍙傛暟鍖栨柟闈粛澶勪簬"formative stage"銆?
# Reproducibility Status / 鍙鐜版€х姸鎬?
> Literature Card: lightweight screening. Paper Note / Paper Logic: deep analysis.

## Code Availability

**Status**: [x] Available [ ] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

**URL**: https://github.com/seisman/seisbench (SeisBench framework cited)

## Data Status / 鏁版嵁鐘舵€?
- [x] **Public dataset available** 鈥?multiple public datasets cited
- [ ] Restricted dataset
- [ ] Private dataset
- [ ] Unknown

**Dataset Link**: https://ncedc.org/ (NCEDC), https://www.data.jma.go.jp/ (JMA)

## Reproduction Feasibility / 澶嶇幇鍙鎬?
**Overall Assessment**: [x] High [ ] Medium [ ] Low

**Reason**: 缁艰堪璁烘枃鏈韩涓嶆秹鍙婂鐜般€備絾鍏跺紩鐢ㄧ殑澶氭暟鏂规硶锛圥haseNet, EQTransformer, SeisBench锛夊潎鏈夊紑婧愪唬鐮佸拰鍏紑鏁版嵁闆嗐€?
**Notes / 澶囨敞**:
- 璁烘枃鏈韩鏄患杩帮紝鏃?澶嶇幇"姒傚康
- 浣嗗紩鐢ㄧ殑EQTransformer銆丼eisBench绛夊伐鍏蜂唬鐮佸紑婧?
## Zotero

**Status**: Imported
**Item Key**: M8TB5AYY
<!-- Previously not imported, now verified in Zotero storage. -->

# My Decision / 鎴戠殑鍐冲畾

- [ ] Read deeply / 绮捐
- [x] Keep reference / 淇濈暀鍙傝€?- [ ] Ignore / 蹇界暐

**Reason / 鐞嗙敱**: Annual Review绾у埆缁艰堪锛屼环鍊煎湪浜庡叏鏅紡浜嗚ВML鍦伴渿瀛﹀彂灞曡剦缁溿€備絾宸叉湁Monteiro 2024缁艰堪瑕嗙洊閮ㄥ垎閲嶅彔鍐呭銆備綔涓篟eference淇濆瓨锛岄渶瑕佹椂鏌ラ槄鐗瑰畾瀛愰鍩熺珷鑺傘€?
# Related Knowledge / 鐩稿叧鐭ヨ瘑閾炬帴

- Task: [[Seismic Phase Picking]]
- Method: [[PhaseNet]], [[Transformer]], [[Attention Mechanism]]
- Dataset: [[EGS Collab SURF]]



