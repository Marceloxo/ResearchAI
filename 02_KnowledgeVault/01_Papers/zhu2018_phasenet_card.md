---
title: "PhaseNet: a deep-neural-network-based seismic arrival-time picking method"
authors: [Zhu, Beroza]
year: 2019
venue: "Geophysical Journal International"
task: [Seismic Phase Picking]
method: [PhaseNet, U-Net, CNN]
dataset: [NCEDC]
code_available: Available
importance: high
reading_status: done
tags: [phasenet, cnn, phase-picking, deep-learning, zhu-beroza]
created: 2026-07-09
---

# Basic Information / 鍩烘湰淇℃伅

- **Title**: PhaseNet: a deep-neural-network-based seismic arrival-time picking method
- **Authors**: Weiqiang Zhu and Gregory C. Beroza
- **Year**: 2019 (Published online Oct 2018)
- **Venue**: Geophysical Journal International, Vol. 216, pp. 261-273
- **Task**: Seismic Phase Picking (P and S waves)
- **Method**: PhaseNet (modified U-Net for 1D time series)
- **Dataset**: NCEDC (Northern California Earthquake Data Center)
- **Code**: Available

# Research Problem / 鐮旂┒闂

> 浜哄伐鎷炬尝鍔冲姩瀵嗛泦涓旀槗鍑洪敊锛屼紶缁熻嚜鍔ㄦ嬀娉㈠櫒绮惧害涓嶅浜虹被涓撳銆侾haseNet鐢ㄦ繁搴﹀涔犺嚜鍔ㄦ嬀鍙朠/S娉㈠埌杈炬椂闂淬€?
# Main Contribution / 涓昏璐＄尞

> 鎻愬嚭PhaseNet 鈥?涓€涓慨鏀硅嚜U-Net鐨凜NN鏋舵瀯锛岀洿鎺ヤ粠鏈护娉㈢殑涓夊垎閲忓湴闇囨尝褰腑棰勬祴P娉€丼娉㈠拰鍣０鐨勬鐜囧垎甯冿紝宄板€煎嵆涓哄埌杈炬椂闂淬€傚湪NCEDC鏁版嵁闆嗕笂杈惧埌杩滆秴浼犵粺AR鎷炬尝鍣ㄧ殑绮惧害銆?
# Method Overview / 鏂规硶姒傝堪

> 灏哢-Net鐨?D鍗风Н鏀逛负1D鍗风Н锛岃緭鍏?0绉掍笁鍒嗛噺娉㈠舰(3脳3001)锛岃緭鍑轰笁涓鐜囧垎甯?P/S/鍣０)銆備娇鐢ㄩ珮鏂帺鐮佸皢浜哄伐鏍囨敞杞寲涓鸿蒋鏍囩銆傝缁冩暟鎹?79,514鏉℃尝褰紝623K璁粌/78K楠岃瘉/79K娴嬭瘯銆?
# Dataset and Evaluation / 鏁版嵁闆嗕笌璇勪及

- **NCEDC**: 30骞村寳鍔犲窞鍦伴渿鏁版嵁锛?79,514鏉℃爣娉ㄦ尝褰?- **璇勪及鎸囨爣**: Precision, Recall, F1 Score, 娈嬪樊鍧囧€?鏍囧噯宸?- **鍩虹嚎**: AR Picker (ObsPy)

# Why This Paper Matters / 涓轰粈涔堝叧娉ㄨ繖绡囪鏂?
> PhaseNet鏄湴闇嘇I棰嗗煙鐨勫鍩烘€у伐浣滀箣涓€銆傚畠鏄疌hai 2020杩佺Щ瀛︿範鐨勮捣鐐癸紝涔熸槸鍚庣画浼楀鍦伴渿DL鐮旂┒鐨勫熀绾挎柟娉曘€傚叾U-Net鈫?D CNN鐨勬敼閫犳€濊矾鍙縼绉诲埌鍦伴渿鍥惧儚鍒嗗壊浠诲姟銆?
# Limitations / 灞€闄愭€?
> 璁粌鏁版嵁浠呮潵鑷寳鍔犲窞锛屽煙澶栨硾鍖栨€ф湭鐭ャ€傛湭浣跨敤甯﹂€氭护娉㈤澶勭悊鎰忓懗鐫€妯″瀷瀛﹀埌浜嗗櫔澹扮壒寰併€傛湭娴嬭瘯杩炵画鏁版嵁涓婄殑妫€娴嬭兘鍔涖€?
# Reproducibility Status / 鍙鐜版€х姸鎬?
> Literature Card: lightweight screening. Paper Note / Paper Logic: deep analysis.

## Code Availability

**Status**: [x] Available [ ] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

**URL**: https://github.com/weiqiangzhu/PhaseNet

## Data Status / 鏁版嵁鐘舵€?
- [x] **Public dataset available** 鈥?freely downloadable from NCEDC
- [ ] Restricted dataset
- [ ] Private dataset
- [ ] Unknown

**Dataset Link**: https://ncedc.org/

## Reproduction Feasibility / 澶嶇幇鍙鎬?
**Overall Assessment**: [x] High [ ] Medium [ ] Low

**Reason**: 浠ｇ爜寮€婧愶紝鏁版嵁闆嗗叕寮€锛屾灦鏋勬竻鏅帮紝璁粌缁嗚妭瀹屾暣銆?
**Notes / 澶囨敞**:
- 璁烘枃鏈彁鍙婇殢鏈虹瀛?- 鏈彁鍙妑equirements.txt鎴朌ockerfile
- 杈撳叆30s脳100Hz脳3鍒嗛噺锛岃绠楅噺涓嶅ぇ锛孯TX 4070鍙繍琛?
## Zotero

**Status**: Imported
**Item Key**: 2U6E8WAQ

# My Decision / 鎴戠殑鍐冲畾

- [x] Read deeply / 绮捐
- [ ] Keep reference / 淇濈暀鍙傝€?- [ ] Ignore / 蹇界暐

**Reason / 鐞嗙敱**: PhaseNet鏄湴闇嘇I棰嗗煙鐨勫鍩烘€у伐浣滐紝鏄疌hai 2020杩佺Щ瀛︿範鐨勮捣鐐癸紝涔熸槸鍚庣画浼楀鐮旂┒鐨勫熀绾挎柟娉曘€傚叾U-Net鈫?D CNN鏀归€犳€濊矾瀵瑰湴闇囧浘鍍忓垎鍓叉湁鐩存帴鍙傝€冧环鍊笺€?
# Related Knowledge / 鐩稿叧鐭ヨ瘑閾炬帴

- Task: [[Seismic Phase Picking]]
- Method: [[PhaseNet]], [[U-Net]], [[CNN]]
- Dataset: [[EGS Collab SURF]]

