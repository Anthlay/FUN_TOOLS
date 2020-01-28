import random
list_prefix = [
('smug' , '光 光滑 滑溜 ','smuggle 走私 v'),
('init' ,'开始','initiate 开始 创始 启蒙'),
('germ','seed 种子',' germ 细菌 幼芽 病原菌'),
('infra' ,'下 低','inferior 下级 晚辈 次品'),
('val' ,'价值','value 重视 尊重 评价'),
('con' ,'强调 一起 强化',' 前缀'),
('cept' ,'抓住','concept 观念 con 强调'),
('rue' ,'后悔的 悲伤的','ruthless 无情的 冷酷的'),
('slit ' , '切开 切口 ' , ' slit' ),
('riot' , ' 骚乱 暴乱' , 'riot ' ),
('frag' , 'break 折断 ' , ' fragile 脆的 体质弱的' ),
('scorch ' , '烧焦 枯萎挖苦 ' , ' scorch' ),
('quartz ' , '石英 ' , 'quartz ' ),
(' de' , ' 去掉 离开 相反 整个 加强 ' , 'de 前缀' ),
('prive' , ' 自己的' , ' deprive  夺去' ),
('syn sym ' , '共同 相同 ' , ' 前缀' ),
('thes ' , '放置 ' , ' synthesis 合成 综合 综合物' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
(' ' , ' ' , ' ' ),
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