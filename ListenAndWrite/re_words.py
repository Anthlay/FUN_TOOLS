import random
list_prefix = [ ('a-' , '否','asymmetry（不对称)'),
('an-' ,'否','anhydrous（无水的）'),
('dis-','否',' dishonest'),
('in-' ,'否','incapable inability'),
('il-' ,'否','illegal'),
('ig-' ,'否','ignoble'),
('im-' ,'否','impossible immoral'),
('ir-' ,'否','irregular'),
('ne-' ,'否',' never' ),
('n- ' ,'否','neither'),
('non-' ,'否','none '),
('neg-' ,'否','neglect' ),
('un-' ,'否','unable'),
('male-','错误',''),
('mal-' ,'错误' ,'malfunction  失调 '),
('mis-' ,'错误','mistake '),
('pseudo-','错误','pseudonym假名 '),
('de- ','反动作', 'demodulation解调 '),
('dis-' ,'反动作','disarm '),
('un- ','反动作','unload '),
('anti-',' 相反',' antiforeign 排外的  '),
('ant- ','相反',' antiknock 防震 '),
('contra-',' 相反','contradiction'),
('contre-',' 相反',''),
('contro-',' 相反 ','controflow 逆流 '),
('counter- ','相反','counterreaction '),
('ob-','相反','  object'),
( 'oc-','相反','  occupy '),
( 'of-','相反  ',''),
('op- ','相反',' oppose '),
('with-',' 相反',' withdraw '),
('a- ','’’表示“ 在??之上” ，“向??”',' aboard aside '),
('by-',' 表示“附近，邻近，边侧 ”',' bypath bypass弯路 '),
('circum-',' 表示“周围，环绕，回转 ”',' circumstance circuit '),
('circu- ','表示“周围，环绕，回转 ”',' circumstance circuit '),
('de-',' 表示“在下，向下 ”',' descend degrade '),
('en- ','表示“在内，进入 ”',' encage（禁闭）  enbed上床 '),
('ex- ec- es-',' 表示“外部，外 ”',' exit eclipse expand export '),
('extra-',' 表示“额外”',' extraction （提取）'),
('fore- ','表示“在前面”',' forehead foreground '),
('in- il- im- ir- ','表示“向内，在内，背于 ” ','inland invade inside import '),
('inter- intel- ','表示“在??间，相互 ” ','international interaction internet '),
('intro-',' 表示“向内，在内，内侧 ”',' introduce introduce '),
('medi- med- mid- ','表示“中，中间 ” ','Mediterranean midposition '),
('out- ','表示“在上面，在外部，在外 ” ','outline outside outward '),
('over- ','表示“在上面，在外部，向上 ”',' overlook overhead overboard '),
('post-',' 表示"向后，在后边，次 ” ','postscript附言，'),
('pre-',' 表示"在前”在前面” ','prefix preface preposition '),
('pro- ','表示“在前，向前 ” ','progress proceed '),
('sub- suc- suf- sug- sum- sup- sur- sus- ','表示“在下面，下 ”','subway submarine suffix suppress supplement' ),
('trans- ','表示“移上，转上，在那一边 ”',' translate transform transoceanic '),
('under- ','表示“在?下面，下的 ” ','underline underground underwater '),
('up- ','表示“向上，向上面，在上 ” ','upward uphold uphill上坡 '),
('ante- anti- ','表示“先前，早于，预先 ”','antecedent anticipate '),
('ex-',' 表示“先，故，旧 ”','expresident exhusband '),
('fore-',' 表示“在前面，先前，前面 ”','foreward dorecast foretell预言 '),
('mid- medi- ','表示“中，中间 ”','midnight midsummer '),
('post-','"表示“在后，后 ”','postwar '),
('by-',' 表示“副，次要的 ”','byproduct bywork副业 '),
('extra-','表示“超越，额外 ”','extraordinary '),
('hyper-',' 表示“超过，极度 ”','hypersonic超声波  hypertesion高血压  '),
('out-','表示“超过，过分 ”','outdo超过 outbid出价过高的人  '),
('over-','，表示 “超过，过度，太 ”','overeat overdress oversleep '),
( 'sub- suc- sur-','   表示“低，次，副，亚 ”','subeditor subordinate subtropical亚热带'),
('super- sur-',' 表示“超过”','Supernature  superpower  surplus  surpass '),
('under-','表示“低劣，低下 ”','undersize undergrown underproduction生产不足  '),
('pre- pri-',' 表示“在前，事先，预先 ”','preheat prewar prehistory '),
('pro- ','表示“在前，先，前 ”','prologue 序幕，prophet预言家 ' ),
('re- ','表示“再一次，重新 ”','retell rewrite '),
('vice- ','表示“副，次 ”','vicepresident vicechairman'),
('com- cop- con- cor- co- ','表示“共同，一起 ” 。','connect combine collect combat coexist co-operate '),
('syn- syl-sym-','表示“同，共，和，类 ”','symmetry sympathy synthesis合成 '),
('al-',' 表示“完整，完全 ”','alone almost '),
( 'over-','表示“完全，全 ”','overall overflow充满 '),
( 'pan-','表示“全，总，万 ”','panentheism泛神论 ，panorama'),
('a- ab- abs-','表示“分离，离开 ”',' away apart abstract abstain '),
('de-',' 表示“离去，处去 ”','depart decolour '),
('dis- di- dif- ','表示“分离，离开 ”',' divorce disarm缴械 '),
('ex- e-',' 表示“离开，分离 ”','expel exclude expatriate驱出国外  '),
('for-',' 表示“离开，脱离 ”','forget forgive '),
('re-','表示“离开”','release resolve '),
('se-','表示“分离，隔离 ”','separate seduce select '),
('dia-','表示“通过，横过 ”','diameter diagram '),
('per- pel- ','表示“通，总，遍 ”','perfect perform pervade浸透 '),
('trans-',' 表示“横过，贯通 ”','transparent transmit transport '),
('a-',' 加强','arouse ashamed '),
('ad-',' 加强','adjoin adhere 粘着 '),
('be- ','变换词类作用','befriend '),
('en- ','变换词类作用','enslave enable enrich '),
('ad-','变换词类作用','adapt'),
( 'ac-',' 变换词类作用','accord '),
('af- ','变换词类作用','affix'),
('ag- ','变换词类作用','aggression arrive'),
('an-','变换词类作用',''),
( 'ap- ','变换词类作用',''),
('ar-','变换词类作用','arrange '),
( 'as-','变换词类作用','assist assign委派'),
( 'at-','变换词类作用','attend attract '),
('mono-','单','monotone单调'),
('mon- ','单',' monarch '),
('uni-','单',' uniform'),
( 'un-','单 ',' unicellular单细胞  '),
('ambi-','双',' ambiguous amphibian两栖类  '),
('bi-','双',' bicycle '),
( 'bin- ','双',''),
('di-','双',' diode二级管 ，'),
('twi- ','双','twilight '),
('deca -','“十”',' decade '),
('deco- ','“十”',''),
('dec-','“十”',' decade '),
( 'deci-','“十”','decimals '),
('hecto-','百，百分子一',' hect- hectometer '),
('centi- ','百，百分子一','centimeter '),
('kilo- ','千，千分子一',' kilometer '),
('myria- ','万，万分子一','myriametre'),
('myri- ','万，万分子一','myriametre '),
('mega-',' 万，万分子一','megabyte '),
('meg- ','万，万分子一',' megabyte '),
('micro- ','万，万分子一',' microvolt 微伏特  '),
('multi-',' 许多','multipmetre 万用表'),
('mult- ','许多','multipmetre 万用表  '),
('poly- ','许多',' polysyllable '),
('hemi- ','一半','hemisphere '),
('demi-',' 一半',' demiofficial '),
('semi-',' 一半',' semiconductor semitransparent '),
('pene-',' 一半 ”',''),
('pen-  ','一半',' peninsula '),
('arch- ','表示“首位，第一的，主要的 ”','architect archbishop '),
('auto-',' 表示“自己，独立，自动 ”','automobile autobiography '),
('bene- ','表示“善，福”','benefit '),
('eu- ','表示“优，美好 ”','eugenics优生学 ，euphemism '),
('male-','表示“恶，不良 ”','maltreatment malodor '),
('mal- ','表示“恶，不良 ”','maltreatment malodor '),
('macro- ','表示“大，宏大 ”','macroscopic宏观 '),
('magni- ','表示“ 大”','magnificent '),
('micro- ','表示“微”','microscope '),
('aud-',' 表示“听，声”','audience '),
('bio-',' 表示“生命，生物 ”','biography传记 '),
('ge- ','表示“地球，大地 ”','geography '),
('phon-',' 表示“声，音调 ”','phonograph '),
('tele- ','表示“远离”','television telephone '),
(' -ize','表示“使成为；使形成；使……化”之意。','realize  v 实现；实行'),
(' -ify','表示“使成为；使形成；使……化”之意。','beautify  v美化'),
(' -en','表示“变为；变得；使变得”之意 ',' shorten  v（使）变短；缩短'),
(' -less','表示“无；缺；没有”等含义。','homeless  adj 无家的；无家可归的'),
(' -able','表示“能够……的；值得……的；有……性质的”等含义。','reasonable  adj合理的；有道理的'),
('-ful','表示“充满……的；容易……的；赋有……性质的”等含义。','helpful  adj 有帮助的；有用的'),
('-ant,-ent','表示人或构件',' applicant 申请人 component(部件，成分)，' ),
('-ee','在动词后面，表示动作的接受者 ','employee（被雇佣者），abandonee（受领被抛弃财物者）， addressee（收件人），refugee （难民）' ),
('-eer','表示“从事于……的人”',' engineer（工程师），profiteer（投机者），pioneer（先 锋），volunteer（志愿者） '),
('-or指人或物',' accelerator（加速器），accumulator（蓄电池、存储器），actor（演员），collector （收集者） '),
('-graph','用于写或记录的机械',' ammograph（风速什），chorograph（位置测定器），seimograph（地震仪）。 '),
('-ian,-an,-ese','指大陆、国家的人 ','African（非洲人），American（美国人），Asian（亚洲人），Japanese（日本人），Chinese（中国人） '),
('-ician','指熟悉……人 ',' electrician（电工），logician（逻辑学家）， mathematician（数学者） '),
('-ist','指相信  某种理论或制度或经常做某项工作的人 ','botanist（植物学家） '),
('-miter,-meter','仪器',' tachmiter（视距仪，准距仪），tromometer（微震仪）。 '),
('-ism','主义 ','socailism（社会主义），capitalism（资本主义） '),
('-ard','指人，带轻蔑意味',' drunkard（醉鬼），coward（胆小鬼） '),
('-ette','小，（商业上）表示假的',' cigarette（香烟），kitchenette（小厨房），essayette （短论文），storyette（短篇小说）。 '),
('-y,-ie','加在称呼上表示亲昵',' Deary（亲爱的），daddy（爸爸），granny（奶奶、姥姥） ，shorty（短衣服） '),
('-let','小（加在名词后面）',' booklet（小册子），streamlet（小溪） '),
('-ling','小（带有轻蔑的意思）',' lordling（愧儡王），professorling（小教授），weakling（窝囊废），hireling（市侩） '),
('-age','加在动词后面，表示行为的结果 ','stoppage（阻塞），storage（储藏），marriage（婚姻） ，stortage（短缺） '),
('-al','加在动词后面 ','approval（建议），denial（否认），refusal（拒绝）， rehearsal（彩排） '),
('－cy','构成名词 ','accuracy（正确性），diplomacy（外交），constancy （经常），bankruptcy（破产） '),
('-dom','表示国家，职业，状况 ','freedom（自由），martyrdom（殉难），kingdom（王国） ，wisdom（智慧） '),
('-ful','加在容器后面，表示某容器的容量 ','handful（一把的），mouthful（一口之量的），glassful （一杯之量的） '),
('-hood','为名词后辍，表示关系或抽象意义',' brotherhood兄弟)，fatherhood（你辈），neighborhood （邻居），likelihood（可能性） '),
('-it, is','表示“炎症”',' bronchitis（支气管炎），arthritis（关节炎）， appendicitis（阑尾炎） '),
('-ity','加在形容词后面，表示抽象意义 ','ability（能力），reality（现实） '),
('-ness','是最活跃的后缀之一，可以加在许多形容词后，构成抽象名词 ','friendliness（友好），kindness（和蔼）， progressiveness（进步） '),
('-gram','构成“画、图、字”等含义',' diagram（图表，图解），program（计划），telegram（电 文，电报） '),
('-ship','加在名词后面，表示状态、抽象概念',' friendship（友谊），relationship（关系）， membership（成员），citizenship（居民权）' ),
('-try,-ery','加在名词、形容词、动词后面，表示集体，地点 ','archery（箭术），fishery（渔场），brewery（酿酒厂） ，forestry（林业） '),
('-th','是名词后辍',' birth（出生），death（死亡），depth（深度），growth （生长），strength（力量），truth（真理） '),
('-ty','加在形容词后面，表示特性或情况',' bounty（慷慨，好施），cruelty（残酷），loyalty（忠诚），plenty（多），safety（安全）' ),
('-ure','加在动词后面，表示行为及其结果',' disclosure（说出，透露），expenditure（花费），exposure（展现，暴露），picture（图画）' ),
('-ics','主要表示一门学问',' acoustics（声学），aerobatics（技巧飞行）， economics（经济学）， mechanics（机械学） '),
('-logy','表示一门学科',' archaeology（考古学），biology（生物学），etymology （词源学），geology（地理学） '),
('-nomy',' astronomy（天文学）','，economy（经济），taxonomy（分类学) '),
('-al','加在地名上',' African（非洲的），Australian（澳大利亚的），Canadian（加拿大的） '),
('-ern','表示方向 ','eastern（东方的），northern（北方的），southern（南方的），western（西方的） '),
('-ese ','表示人 ','Japanese（日本人），Chinese（中国人），Vietnamese （越南人） '),
('-ic','加在名词后面 economic','（经济的），specific（特殊的），scientific （科学的） '),
('-ical','加在名词后面 economical','（经济的），historical（历史的）political（政治的） '),
('-ish ','加在国家名称后面，表示该国的或者该国的人加在普通名词后面，表示“具有……性质”，或者含有轻蔑的意思。  加在表示颜色的形容词后面，表示“略带……颜色的”。 ','Swedish（瑞典的）  Childish（幼稚的），womanish（女人气的），foolish（愚昧的），selfish（自私的）。Greenish（微绿的），yessowish（微黄色的）。 '),
('-ar','加在外词后面，构成形容词 ','annular（环状的），familiar（熟悉的），linear（线的），angular（角的） '),
('－ed','加在名词后面，构成形容词 ','aged（年长的），cultured（有文化的），skilled（有技术的），wretched（可怜的） '),
('-fold','加在数词或名词后，构成形容词','threefold（三倍的），tenfold（十倍的），thousandfold（千倍的），manifold（许多倍的） '),
('-id','构成形容词',' acid（酸的），acrid（刻薄的） '),
('-ing','加在动词后面，构成形容词 ','appetizing（开胃的），encouraging（鼓舞人心的），exciting（令人激动的），interesting（有趣的）。' ),
('-less','加在名词后面，构成与之反义的形容词 ','armless（无手臂的）boundless（无限的）countless（不可数的），faithless（背信弃义的） '),
('-proof','加在名词之后，表示“防…的”形容词',' airproof（防气的）soundproof（隔音的）bombproof （防炸弹的），burglarproof（防盗的）' ),
('-some','加在形容词后，构成形容词',' fulsome（过度的，讨厌的），gladsome（愉快的）， tiresome（疲惫的），lonesome（孤独的）'),
('-ious,-uous,-eous','构成形容词',' various（多种多样的），continuous（继续的）， courageous（有勇气的） '),
('-en','加在名词后面，构成动词',' lengthen（加长），frighten（恐吓） '),
('-ate,-ute ','accumulate（集中）','formulate（形成），calculate（计算），attribute（归功） '),
('-en','加在名词、形容词后面 ','blacken（使……黑），broaden（扩宽），deepen（加深） ，fasten（加快），thicken（加厚） '),
('-ify','加在名词、形容词后面',' acidify, alkalify（碱化），beautify（美化）， electrify（使充电），certify（肯定），modify（修正） '),
('-ize,-ise,-yxe,-yse ','Americanize（美国化）','democratize （民主化），modernize（现代化），popularize（通俗化，推广） '),
('-er',' batter 猛打','flatter（吹捧），chatter（喋喋不休地说），whisper（耳语） '),
('-ly','加在形容词后面 ','immediately（立即），quickly（快的），namely（即，就是说） '),
('-ways,-wise,-ward','加在名词或代词后面 ','endways（末端向上地），endwise（末端向下地）lengthways（纵长地）lengthwise（纵长地）'),
('–able  后缀，“……的”',' countable    suitable'),
('–age  后缀，表示状态，行为或结果',' storage    usage'),
('–al, -ial  后缀，表示状态，行为或结果',' removal    proposal'),
('–ance, -ence, -ancy, -ency   后缀',' importance    frequency'),
('–ant, -ent  后缀',' resultant    constant'),
('–ant, -ent  后缀',' important    different'),
('–er  ','表示“……人”，“……者”，工具，用品',' reader    computer'),
('–eur ',' 表示“……人”，“……者”',' rapporteur    saboteur'),
('–fold  ','接在数词后面构成a或ad表示“……倍”',' three-fold'),
('–free  ','后缀，表示“无……的”或“免于……的”',' duty-free    nuclear-free zone'),
('–ful  ','后缀，表示“充满……的”，“有……的”',' useful    successful'),
('–ic, -ical  ',' metallic    political)'),
('–ician  ','后缀，表示“……精通者”“……家”',' mathematician    technician'),
('–ics  ','表示“……学”',' electronics    physics'),
('–ify  ','后缀，表示“使……”，“……化”',' amplify    classify'),
('–sion, -tion  ','后缀',' construction    division'),
('–ish   ','后缀，表示“略带……色的”',' reddish'),
('–ism  ','后缀，表示“……主义”',' communism'),
('–ist  ','后缀，表示“……者”',' physicist    scientist'),
('–ive','  后缀，表示“……的”',' active    productive'),
('–ize ise','后缀，表示“……化”',' mechanize    organize'),
('–less ',' 后缀，表示“没有……的”',' useless    limitless'),
('–logy',' 后缀，表示“……学”',' geology    biology'),
('–ly  ','后缀',' slowly    possibly'),
('–ment','  后缀，表示状态，行为或结果',' movement    development'),
('–meter','  后缀，表示“……仪”',' thermometer    voltmeter'),
('–metry','  后缀，表示“……测量”，     “……学”',' geometry    trigonometry'),
('–ness ',' 后缀',' hardness    usefulness'),
('–or  ','后缀，表示人或物',' operator    conductor'),
('–proof ',' 后缀，表示“防……的”',' water-proof    light-proof'),
('–th ',' 后缀，表示“……度”',' length    width'),
('–ty  ','后缀，表示性质，状态',' density    ability '),
('–wards','  后缀，表示“向……”',' forwards)    upwards)'),
('–y  ','后缀，表示“有……的”',' muddy    watery'),
(' ag',' ag = do ， act 做，动','agent ag做，办理，ent名词后缀，表示人；做事者，“办理人” 代理人'),
(' agri ','   agri = field 田地，农田 (agri 也作 agro, agr)',' agriculture agri 田地，农田，cult 耕作 –ure 名词后缀 '),
(' ann',' ann = year 年 （ann也作enn）',' annual ann 年，-ual 形容词后缀，……的 每年的，年度的'),
(' audi',' audi=hear 听 （audi也作audit）',' audience audi听，-ence名词后缀 听众，倾听'),
(' bell',' bell=war战争',' rebel re-相反，bel(l)战争，战斗；“反戈”，“反战” 反叛，反抗'),
(' brev',' brev=short短','brevity brev短，-ity名词后缀 （陈述等的）简短，简洁；（生命等的）短暂，短促'),
(' ced',' ced=go行走（ced也作ceed，cess）','preceding pre-先，前,见上，-ing形容词后缀，…的 在前的，在先的'),
(' cept',' cept=take 拿，取',' accept ac-加强意义，cept拿→接 接受，领受，承认'),
(' cid，cis',' cut，kill 切，杀 ','decide de-表示加强意义，cid切，切断→裁断→裁决 决定，裁决，判决，下决心'),
(' circ',' circ=ring环，圆','circular circul=circle圆，-ar形容词后缀，…的 圆形的，环形的'),
(' claim，clam',' =cry，shout 喊叫','exclaim ex-外，出，claim叫，“大声叫出” 呼喊，惊叫'),
(' clar',' clar=clear 清楚，明白','clarify clar=clear清楚，明白，-i-，-fy 动词后缀，使…；“使明白” 讲清楚，阐明，澄清'),
(' clud',' clud=close，shut关闭（clud也作clus）','include in-入，内，clud关闭；“关在里面”，“包入” 包含，包括，包住，关住'),
(' cogn',' cogn=know知道','precognition pre-预先，cogn知道，-ition名词后缀 预知，预察，预见'),
(' cord',' cord=heart心','cordial cord心，-ial形容词后缀，…的 衷心的，诚心的'),
(' corpor',' corpor=body （corpor也作corp）','corporator corpor体→团体，-ator表示人 社团或公司的成员'),
(' cred',' cred=believe，trust 相信，信任','incredible in-不，credible可信的 不可信的'),
(' cruc',' cruc=cross十字','cruciform cruc十字，-form形容词后缀，有…形状的 十字形的'),
(' cur','cur=care关心，挂念，注意','curious cur关心，注意，-ious形容词后缀 “引人注意的” 新奇的，奇怪的；'),
(' cur，curs，cour，ccurs','cur，curs，cour，ccurs=run跑','course cours跑→行进 行程，进程，路程，道路，课程'),
(' dent','dent=tooth牙齿','dentist dent牙，-ist表示人；“医治牙病的人” 牙科医生'),
(' di','di=day日','dial di日，-al名词后缀，表示物 日晷，电话机拨号盘（该物圆形似日晷）'),
(' dict','dict=say言，说（dict也作dic','）dictation 见上，-ion名词后缀 口授，命令，支配，口述，听写'),
(' dit','dit=give给','edit e-出，dit给，“给出”→发表，出版；将稿件编好以备发表 编辑'),
(' don','don=give给（don也作do ）','donor don给，赠给，-or表示人 赠给者，捐献者'),
(' du','du=two二','dual du双，二，-al形容词后缀，..的 二重的，双的，二元的'),
(' duc','duc，duct=lead引','introduce intro-入，duc引；“引入” 引进，介绍'),
(' ed','ed=eat吃','edible ed吃，-ible形容词后缀，可…的 可以吃的，食用的'),
(' equ',' equ=equal等，均，平','equal equ相等，-al形容词后缀，…的 相等的，平等的，相同的'),
(' ev','ev=age年龄，寿命，时代，时期 ','longevity long长，ev年龄，寿命，ity名词后缀 长寿，长命'),
(' fact','fact=do，make做，作（fact也作fac）','manufacture manu手，fact作，制作；“用手制作”'),
(' fer','fer=bring，carry带拿','confer con共同，一起，fer拿；把意见“拿到一起来” 协商，商量，交换意见'),
(' flor','flor=flower花(flor也作flour)','florist flor花，-ist表示人 种花者，花卉研究者'),
(' flu','flu=flow流',' fluency flu流，-ency名词后缀 流利，流畅'),
(' fus','fus=pour灌，流，倾泻','confuse con-共同，合，fus流;’合流”，’流到一处”→混在一起 使混杂，混乱，混淆，使迷乱'),
(' grad','grad=step，go，grade步，走，级','gradual grad步，-ual形容词后缀，…的 逐步的，逐渐的'),
(' gram','gram=write，something written of drawn 写，画，文字，图形','grammar gram写，文字，m重复字母，-ar名词后缀;关于’文字的法则 语法，文法'),
(' graph','graph=write，an instrument for making records 写，画，文字，图形，记录器 ','photograph '),
(' gress','gress=go，walk行走 ','congress con-共同’大家走到一起来”→共聚一堂→开会→会议 (代表)大会，国会，议会 '),
(' habit',' habit=dwell居住 ','habitant habit居住，-ant表示人 居住者cohabit co-共同，habit居住 (男女)同居，姘居 '),
(' hibit','hibit=hold拿，持 ',' inhibit in-表示in，’to hold in”，’to maintain in” 阻止，禁止，抑制 '),
(' hospit','  hospit=guest客  ','hospitalize -ize动词后缀 把…送入医院治疗 '),
(' idio',' idio=peculiar，own，private，proper特殊的，个人的，专有的','idiograph graph写，文字，图形 个人的签名，商标 '),
(' insul',' insul=island岛 ',' insulate 使孤立，使与…隔绝 隔离，使孤立，使绝缘 insulin -in名词后缀，表示’素” 胰岛素 '),
(' it','  it=go行走  ','circuit cire圆，环，-u-，-it行 环行，周线，电路，回路 '),

(' ject','ject=throw投掷 ','project pro-向前    投出→拿出，’提出一种设想” 设计，计划，规则'),
(' juven','juven=young年轻，年少  ','juvenile-ile形容词后缀，…的 青少年的;转作名词 青少年'),
(' lect','lect=choose，gather选，收(lect也作leg，lig)  ','elect e-出，lect选;’选出” 选举'),
(' lev',' lev=raise举，升  ','elevate e-出，lev举，-ate动词后缀;’举出”→举起 抬起，举起，使升高'),
(' liber','liber=free自由 ',' liberty liber自由，-ty名词后缀 自由，自由权'),
(' lingu','lingu=language语言  ','collingual col-同，ligua语言，al形容词后缀，…的 (用)同一种语言的'),
(' liter','liter=letter文字，字母 ','literator 见上，-ator表示人 文学家，文人，作家'),
(' loc','loc=place地方 ',' localism 见上，-ism表示主义，语言 地方主义，方言，士语'),
(' log','log=speak言，说 ',' dialogue dia-对，相对， 对话 logic log语言→辩论→推理，论理，-ic名词后缀，表示…学 逻辑'),
(' loqu','loqu=speak言，说  ','eloquent e-出，-ent形容词后缀，…的;’说出的”，’道出的”→能说会道的 有口才的，雄辩的，有说服力的'),
(' lun','lun=moon月亮  ','lunar  月亮的，似月的，新月形的 semilunar semi-半…的 半月形的，月牙形的'),
(' man','man=dwell，stay居住，停留 ',' permanent per-贯穿，从始至终，一直，…的;’一直停留下去的” 永久的，常驻的，常设的'),
(' manu','manu=hand手(manu也作man)',' manual  手册 maintain main→man手，tain持，握;’手持”，’握有” 保持，保存，维持'),
(' mar',' mar=sea海  ','marine 海上的.航海的 submarine 潜入海面下之物  潜水艇'),
(' medi','medi=middle中间',' immediate ;’没有中间空隙时间的”，’当中没有间隔的” 立刻的，直接的'),
(' memor','memor=memory记忆 ','memory  表示情况，状态，行为 记忆，记忆力，回忆，纪念'),
(' merg','merg=dip，sink沉，没(merg也作mers) ',' emerge e-外，’由水中浮出” 浮现，出现   submerge 沉于水中，没入水中'),
(' migr','migr=remove，move迁移  ','  immigrate in-入内，移居入境，(从外国)移来，移入'),
(' milit','milit=soldier兵  ','militia ，-ia表示集合名词 民兵组织，民兵(总称) militarism 见上，-ism主义 军国主义'),
(' mini','mini=small，little小(mini也作min)  ',' minister 现今的部长 大臣，部长  administer ad-表示to，’执行大臣或部长的任务” 管理，施政'),
(' mir','mir=wonder惊奇，惊异 ','  miracle mir惊奇，奇异，-acle表示事物 奇事，奇迹'),
(' miss',' miss=send投，送，发(miss也作mit,mis) ','mission 被派送(委派)出去者” 使团，代表团，使命promise  事先发出 之言 诺言，允诺'),
(' mob','mob=move动 ',' mob mob动→动乱，暴动→暴动的人 暴民;一群暴徒'),
(' mort','mort=death死  ','mortal  终有一死的，死的，临死的 immortal  不死的，永生的，不朽的'),
(' mot','mot=move移动，动 ','motion 表示行为，情况 运动，动promote pro-向前，mor移动;’使向前移动” 推进，促进，提升，升级'),
(' momin',' nomin=name名 ','nominal  名义上的，有名无实的nominate  做…事 提名，任命'),
(' nov','nov=new新  ','novelist 见上，-ist表示人 小说家，小说作者'),
(' numer','numer=number数 ','numerate  -ate动词后缀，做… 计算，计数，数'),
(' onym','onym=name名 ','onymous  有名字的，署名的  anonym  匿名者，无名氏'),
(' oper','oper=work工作','operate 操作，运转，动手术 opera oper工作→动作→表演，作戏→戏 歌剧'),
(' ori',' ori=rise升起  orient ori升起;原义为’太阳升起的地方” 东方，东方的  origin ori升→发生，发起→起源 原始，起源，由来，出身'),
(' paci ','paci=peace和平，平静 ','pacific  和平的，太平的，平静的'),
(' pel ','pel=push，drive推，逐，驱 ','propel  推进，推动expel ex-出，外，赶出，驱逐，开除'),
(' pend ','(a)pend，pens=hang悬挂 ','suspend sus=sub下，pend悬，吊，挂，’挂起来” 挂，悬，中止，暂停'),
(' pet ','pet=seek追求 ','compete 竞争，角逐，比赛 appetite ap-表示to向，pet追求→渴求，渴望 欲望，食欲'),
(' phon ','phon=sound声音 ',' otophone oto耳，phon声音 助听器'),
(' pict ','pict=paint画，描绘 ',' depict de-加强意义，pict绘 描绘，描述'),
(' plen ','plen=full满，全 ',' plenilune plen满，-i-，lun月亮 满月，望月.月满之时'),
(' plic ','plic=fold折，重叠 ','multiplicate multi-多，…的 多重的，多倍的，多样的'),
(' pon ','pon=put放置 ','postpone post-后;’往后放” 推后，推迟，延期compound com-共同’放在一起的” 混合的，化合的，混合物，化合物'),
(' popul ','popul=people人民 ','populace popul人民→平民，-ace名词后缀 平民，大众'),
(' port ','port=carry拿，带，运 ','import im-入，port拿，运;’拿进，运入” 输入，进口export ex-出，port运，拿;’运出去” 输出，出口'),
(' pos ','pos=put放置 ','exposure  揭露，揭发，暴露deposit ’放下”→存放 寄存，存放，存款，储蓄'),
(' preci ','preci=price价值 ','appreciate ap-表示ar或to，preci价值，-ate动词后缀;’论价” 评价，鉴赏，欣赏'),
(' punct ','punct=point，prick点，刺 ','punctuate 加标点于，点标点punctual  ’着于一点的”→限于一点的→不偏不差的 精确的，准确的，准时的'),
(' pur ','pur=pure清，纯，净 ','depurate de-加强意义，-ate动词后缀，使成… 使净化，净化，提纯'),
(' rect ','rect=right，straight正，直 ','correct cor-表示加强意义，rect正，直 改正，纠正，正确的'),
(' rupt ','rupt=break破 ','bankrupt bank=bench长凳 ’钱商的柜台断了”→生意破产了 破产的，破产者，使破产'),
(' sal ','sal=salt盐 ','salary sal(salt)盐，’买盐的钱”，由此转为’工资” 薪金，工资 salad 表示物 色拉，沙拉，一种用盐调拌的凉菜'),
(' scend ','scend，scens=climb爬，攀 ','ascend ’爬上” 上升;登高，攀登 descend  下降，传下，遗传'),
(' sci ','sci=know知 ','conscience con-共同，完全，sci知，-ence名词后缀;’完成知道善恶是非之分” 良心，道德心'),
(' sec，sequ ','sec，sequ=follow跟随 ','sequacious -acious形容词后缀，…的 盲从的'),
(' sect ','sect=cut切割 ','insect 昆虫躯体分节，故名 昆虫 section -ion表示行为及行为的结果 切下的部分，由大机关中’分割”出来的小机关 科，处'),
(' sent ','sent，sens=feel感觉 ',' sentiment  感情，情绪，思想感情，意见 consensus  ;’共同的认识” 共识，意见一致'),
(' sid ','sid=sit坐 ','president 见上，-ent表示;’指挥者”，总统，大学校长，会长，总裁 assiduous  能坐下来坚持工作的” 刻苦的，勤奋的'),
(' sist ','sist=stand站立 ','assist ’立于一旁” 帮助，援助，辅助 insist in-加强意义’坚定不移” 坚决主张，坚持'),
(' son ','son=sound声音 ','sonic ，-ic形容词后缀， 声音的，音速的 supersonic 超音速的'),
(' spect ','spect=look看 ','respect’重复地看”→重视 尊重，尊敬 specimen spec(-spect)看，-i-，men名词后缀;’给人看的东西 样品，样本，标本'),
(' spir ','spir=breathe呼吸 ','conspire ’共呼吸”→互通气息 共谋，同谋，阴谋，密谋策划inspire’吸入”，吸气，注入→注入勇气 鼓舞激励，使生灵感'),
(' tail ','tail=cut切割 ','tailor 剪裁者 裁缝，成衣工，成衣商detail de-加强意义，由整体切碎细分而成的部分 细节，细目，详情，零件'),
(' tain，tan，tin ','tain，ten，tin=hold握，持，守 ','sustain ’在下面支持” 支持，维持，供养maintain main=man手，保持，保存，维持，坚持，供养'),
(' tect ','tect=cover掩盖 ','detect de-除去，取消，tect掩盖;’除去掩盖”→揭露秘密→查明真相 侦查，侦察，发觉'),
(' tele ','tele=far远 (tele现多用以表示与电波有关的事物)','telecontrol tele远，control控制 远距离控制，遥控'),
(' tempor ','tempor=time时 ','temporary 暂时的，临时的contemporary  同时代的人，同年龄的人'),
(' tend ','tend(tends，tent)=stretch伸 ','attend ’把精神或心思伸向…’ 注意，关心，出席attention  注意，关心，注意力'),
(' terr ','terr=earth，land土地，陆地 ','territory  -ory名词后缀 领土，领地terrace ，-ace名词后缀 台地，地坪，平台，阳台'),
(' text ','text=weave编织 ','textile ，-ile名词后缀，表示物 纺织品pretext pre-先，预先，text编织→编造;’预先编造的话” 借口，托词'),
(' tract ','tract=draw拉，抽，引 ','tractor  拖拉机 attract at-=ad-表示to， 吸引，诱惑contract 使二者结合在一起 订约，缔结，契约，合同'),
(' un ','un=one一(un也作uni) ','unite 统一，联合，团结 uniform uni单一，form形式，式样 一样的，相同的，制服'),
(' urb ','urb=city ','suburb sub,下,靠近,郊区,郊外,近郊,城外 urban ，-an形容词后缀，…的 城市的，都市的'),
(' vac','vac=empty空(vac也作vacu) ','vacant  空的，空白的，未被占用的  vacuum-um名词后缀 真空，真空状态，真空度'),
(' vad ','vad(vas)=walk，go行走 ','invade ’走入”→闯入 侵入，侵略，侵犯'),
(' vari ','vari=change ','variable ，-able形容词后缀，可…的 可变的，反复不定的 variety ，-ety名词后缀，表示情况，性质 变化，多样化，种种'),
(' ven ','ven=come来 ',' intervene ;’来到其间”→介入其中 干预，干涉，介入convene ;’召唤大家来到一起” 召集(会议)，集合'),
                ]
#count = 0


#英译汉
def judge_y():
    count = 0
    while(True):
        id = random.randint(1, 267)
        output_list = list_prefix[id]
        print('>>>> '+output_list[0]+' <<<< 意为：')
        answer = input('')
        if answer in output_list[1]:
            count += 2
            print('-')
            print('-------YES------------------------------------------')
            #print('-')
            print(output_list[1]+ '  '+output_list[2])
            print("####当前得分： "+str(count)+"     ####")
            print('-----------------------------------------------------')
            print('-')

            if count == 50:
                print('########################')
                print('####                ####')
                print('#### 恭喜玩家得到50分 ####')
                print('####                ####')
                print('########################')


        else:
            print('-')
            print('--------WRONG--------------------------------------------')
            #print('-')
            print(output_list[1]+ '  '+output_list[2])
            print("####   当前得分："+str(count)+"####")
            print('--------------------------------------------------------')
            print('-')
    return count
#汉译英
def judge_h():
    id = random.randint(1, 160)
    output_list = list_prefix[id]
    print(output_list[1])
    answer = input('意为：')
    if answer in output_list[0] :
        print('-')
        print('YES')
        print('-')
        print(output_list[2])
    else:
        print('-')
        print('WRONG')
        print('-')
        print(output_list[1] + '  ' + output_list[2])
        print('-')


if __name__ == '__main__':

    judge_y()