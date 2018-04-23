#coding=utf-8
import urllib2,sys,time,datetime,os,pymysql.cursors
from setting import headers, domain, start_url, file_output

read_file=open("readed.txt","a")
alldatas={}
readed_file = open("readed.txt","r")
for lines in readed_file:
        data = lines.strip("\n")
        alldatas[data]="readed"

connection = pymysql.connect(host='127.0.0.1', port=3306, user='test', password='test', db='cars', charset='gbk', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()





def getTag(data,afterString,betString,beforString):
    ourdata=data[data.index(afterString)+len(afterString):]
    if len(beforString)>0:
        ourdata=ourdata[:ourdata.index(beforString)]
    if len(betString)>0 and betString=="><" and ">"in ourdata and "<" in ourdata:
        ourdata=ourdata[ourdata.index(">")+1:]
        ourdata=ourdata[:ourdata.index("<")]
        return ourdata
    if len(betString)>0 and betString=="<>"and ">"in ourdata and "<" in ourdata:
        if "<" in ourdata and  ">"in ourdata:
            ourdata=ourdata[:ourdata.index("<")]+ourdata[ourdata.index(">")+1:]
            if "<" in ourdata and  ">"in ourdata:
                ourdata=ourdata[:ourdata.index("<")]+ourdata[ourdata.index(">")+1:]
    return ourdata

for n in range(1,50):
    print n
    pageurl=start_url
    if n>1:
        pageurl=" https://www.xin.com/suzhou/i"+bytes(n)+"/"

    try:
 
        carList=urllib2.urlopen(pageurl) 
    except Exception,e:
                print 'openERR:'
                print carList
                print str(e)
    else:
        if carList:
            carListPage=carList.read()
            carListPage=carListPage[carListPage.index("<div class=\"carlist-show\" id=\"search_container\">"):]
            carListPage=carListPage[carListPage.index("<ul>"):carListPage.index("</ul>")]
            carList=carListPage.split("href=\"")
            carList.remove(carList[0])
            for car in carList:
                num=carList.index(car)
                carList[carList.index(car)]="https:"+car[:car.index("\"")]
                print carList[num]
            
            carsnum=len(carList)

            for i in range(0,carsnum):
                try:
                    if carList[i] in alldatas :
                        pass
                        continue
                    try:
            
                        car=urllib2.urlopen(carList[i]) 
                    except Exception,e:
                                print 'openERR:'
                                print carList[0]
                                print str(e)
                    else:
                        if car:
                            carPage=car.read()
                            
                            id=carList[i]
                            data=carPage
                            data = carPage.decode('utf-8').encode(sys.getfilesystemencoding())
                            title=data[data.index("<span class=\"cd_m_h_tit\">")+25:]
                            blank=title[:2]
                            title=title[:title.index("</span>")].strip(title[:2])
                            price=getTag(data,"<span class=\"cd_m_info_jg\">","><","</span>")
                            dataList1=getTag(data,"<ul class=\"cd_m_info_desc\">","","</ul>")
                            dataList1=dataList1.split("</li>")
                            shang_jia=""
                            shang_jia_dian_hua=""
                            shang_jia_zai_shou=""
                            shang_jia_yi_shou=""
                            shang_jia_lei_xin=""
                            shang_jia_di_zhi=""
                            guo_hu=""
                            kou_bei=""
                            jian_jie=""
                            zhi_bao=""
                            tu=""
                            registered_year=getTag(dataList1[0],"<span class=\"cd_m_desc_key\">","<>","</span>")[:4]
                        
                            registered_month=getTag(dataList1[0],"<span class=\"cd_m_desc_key\">","<>","</span>")[6:8]
                           
                            mils=getTag(dataList1[1],"target=\"_blank\" >","","</a>").strip(blank)
                       
                            vehicle_emissions_standard=getTag(dataList1[2],"cd_m_desc_cursor\">","","<").strip(blank)
                           
                            gear=getTag(dataList1[3],"cd_m_desc_val\">","","<").strip(blank)
                        
                            location=getTag(dataList1[4],"cd_m_desc_val\">","","<").strip(blank)
                            
                            
                            
                            dataList2=data.split("</dd>")
                            
                            
                            yong_tu=getTag(dataList2[9],"cd_m_i_pz_val\">","","</span>").strip(blank)
                         
                            nian_jian=getTag(dataList2[10],"cd_m_i_pz_val\">","","</span>").strip(blank)
                        
                            bao_xian=getTag(dataList2[11],"cd_m_i_pz_val\">","","</span>").strip(blank)
                             
                            wei_bao=getTag(dataList2[12],"cd_m_i_pz_val\">","","</span>").strip(blank)
                        
                            ji_bie=getTag(dataList2[14],"cd_m_i_pz_val\">","><","</span>").strip(blank)
                         
                            yan_se=getTag(dataList2[15],"cd_m_i_pz_val\">","><","</span>").strip(blank)
                            
                            fa_dong_ji=getTag(dataList2[19],"cd_m_i_pz_val\">","","</span>").strip(blank)
                         
                            bian_su_qi=getTag(dataList2[20],"cd_m_i_pz_val\">","><","</span>").strip(blank)
                        
                            displacement=bian_su_qi
                            pai_fang=getTag(dataList2[21],"cd_m_i_pz_val\">","><","</span>").strip(blank)
                   
                            ran_you=getTag(dataList2[22],"cd_m_i_pz_val\">","><","</span>").strip(blank)
                      
                            qu_dong=getTag(dataList2[23],"cd_m_i_pz_val\">","><","</span>").strip(blank)
                          
                           
                            che_yuan="YX"
                            sqlValues="\'"+id+"\',\'"+che_yuan+"\',\'"+title+"\',\'"+price+"\',\'"+ mils+"\',\'"+registered_year+"\',\'"+ registered_month+"\',\'"+gear +"\',\'"+ displacement +"\',\'"+location+"\',\'"+ vehicle_emissions_standard+"\',\'"+nian_jian+"\',\'"+bao_xian +"\',\'"+ zhi_bao +"\',\'"+pai_fang+"\',\'"+ guo_hu+"\',\'"+yong_tu+"\',\'"+ wei_bao+"\',\'"+shang_jia +"\',\'"+jian_jie +"\',\'"+fa_dong_ji+"\',\'"+ bian_su_qi+"\',\'"+ji_bie+"\',\'"+ yan_se+"\',\'"+ran_you +"\',\'"+ qu_dong +"\',\'"+kou_bei+"\',\'"+ tu+"\',\'"+shang_jia_dian_hua+"\',\'"+ shang_jia_di_zhi+"\',\'"+shang_jia_zai_shou +"\',\'"+ shang_jia_yi_shou +"\',\'"+shang_jia_lei_xin+"\'"
                           
                            sql ="INSERT INTO `youxin` (`id`, `che_yuan`, `title`, `price`, `mils`, `registered_year`, `registered_month`, `gear`, `displacement`, `location`, `vehicle_emissions_standard`, `nian_jian`, `bao_xian`, `zhi_bao`, `pai_fang`, `guo_hu`, `yong_tu`, `wei_bao`, `shang_jia`, `jian_jie`, `fa_dong_ji`, `bian_su_qi`, `ji_bie`, `yan_se`, `ran_you`, `qu_dong`, `kou_bei`, `tu`, `shang_jia_dian_hua`, `shang_jia_di_zhi`, `shang_jia_zai_shou`, `shang_jia_yi_shou`, `shang_jia_lei_xin`) VALUES (" + sqlValues+ ")"
                            
                    
                            try:
                                    cursor.execute(sql)
                                    connection.commit()
                                    print "sucess at:"+id
                            except Exception,e:
                                
                                if "Duplicate" in str(e) or "PRIMARY" in str(e):
                                        print "try again"
                                        sql ="UPDATE  `youxin` SET `title`=\'"+title
                                        +"\',`che_yuan`=\'"+che_yuan+"\',  `price`=\'"+price
                                        +"\', `mils`=\'"+mils+"\', `registered_year`=\'"+registered_year
                                        +"\', `registered_month`=\'"+registered_month+"\', `gear`=\'"+gear
                                        +"\', `displacement`=\'"+displacement+"\', `location`=\'"+location
                                        +"\',  `vehicle_emissions_standard`=\'"+vehicle_emissions_standard
                                        +"\', `nian_jian`=\'"+nian_jian+"\', `bao_xian`=\'"+bao_xian
                                        +"\', `zhi_bao`=\'"+zhi_bao+"\', `pai_fang`=\'"+pai_fang
                                        +"\', `guo_hu`=\'"+guo_hu+"\',  `yong_tu`=\'"+yong_tu+"\', `wei_bao`=\'"+wei_bao
                                        +"\', `shang_jia`=\'"+shang_jia+"\', `jian_jie`=\'"+jian_jie
                                        +"\', `fa_dong_ji`=\'"+fa_dong_ji+"\', `bian_su_qi`=\'"+bian_su_qi
                                        +"\',  `ji_bie`=\'"+ji_bie+"\', `yan_se`=\'"+yan_se+"\', `ran_you`=\'"+ran_you
                                        +"\', `qu_dong`=\'"+qu_dong+"\', `kou_bei`=\'"+kou_bei+"\', `tu`=\'"+tu
                                        +"\',  `shang_jia_dian_hua`=\'"+shang_jia_dian_hua+"\', `shang_jia_di_zhi`=\'"+shang_jia_di_zhi
                                        +"\', `shang_jia_zai_shou`=\'"+shang_jia_zai_shou+"\', `shang_jia_yi_shou`=\'"+shang_jia_yi_shou
                                        +"\', `shang_jia_lei_xin`=\'"+shang_jia_lei_xin+"\' WHERE (`id`=\'"+id+"\')"
                                        try:
                                                #print "try update"
                                                cursor.execute(sql)
                                                connection.commit()
                                                #print "UPDATED DATA:"+id
                                               # print "update sucess"
                                                try:
                                                    alldatas[carList[i]]="readed"
                                                    read_file.write(carList[i]+"\n")
                                                    read_file.flush()      
                                                except Exception,e:
                                                    print "save err"
                                                    print str(e)
                                                    pass
                                                    continue    
                                        except Exception,e:
                                                print "update fauild"
                                                print str(e)
                                                pass
                                                continue
                                else:
                                        print "sql err"
                                        print str(e)
                                        pass
                                        continue
                            try:
                                alldatas[carList[i]]="readed"
                                read_file.write(carList[i]+"\n")
                                read_file.flush()    
                            except Exception,e:
                                print "save err"
                                print str(e)
                                pass
                                continue
                except Exception,e:
                    print "err"
                    
                    print str(e)
                    pass
                    continue
                                        
                
            try:
                alldatas[pageurl]="readed"
                read_file.write(pageurl+"\n")
                read_file.flush()    
                print len(alldatas)
            except Exception,e:
                    
                print "save err"
                print str(e)
                pass
                continue   
read_file.close()
connection.close()     


        