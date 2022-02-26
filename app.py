# coding: utf-8

import pickle

import pandas as pd
from flask import Flask, render_template, request
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

app = Flask("__name__")

df_1=pd.read_csv("data_final.csv")

q = ""

@app.route("/")
def loadPage():
	return render_template('index_final.html', query="")


@app.route("/", methods=['POST'])
def predict():
    
    '''
    arpu_8
    onnet_mou_8	
    offnet_mou_8	
    roam_ic_mou_8	
    roam_og_mou_8	
    loc_og_t2t_mou_8	
    loc_og_t2m_mou_8	
    loc_og_t2f_mou_8	
    loc_og_t2c_mou_8	
    std_og_t2m_mou_8	
    std_og_t2f_mou_8	
    std_og_mou_8	
    isd_og_mou_8	
    spl_og_mou_8	
    og_others_8	
    total_og_mou_8	
    loc_ic_t2t_mou_8	
    loc_ic_t2m_mou_8	
    loc_ic_t2f_mou_8	
    std_ic_t2t_mou_8	             
    std_ic_t2m_mou_8	
    std_ic_t2f_mou_8	
    spl_ic_mou_8	
    isd_ic_mou_8	
    ic_others_8	
    total_rech_num_8	
    max_rech_amt_8	
    last_day_rch_amt_8	
    total_rech_data_8	
    max_rech_data_8	
    count_rech_3g_8	
    av_rech_amt_data_8	
    vol_2g_mb_8	
    vol_3g_mb_8	
    arpu_3g_8	
    night_pck_user_8	
    monthly_2g_8	
    fb_user_8	
    aon	
    aug_vbc_3g
    '''
    

    
    arpu_8 = request.form['arpu_8']
    onnet_mou_8 = request.form['onnet_mou_8']
    offnet_mou_8 = request.form['offnet_mou_8']
    roam_ic_mou_8 = request.form['roam_ic_mou_8']
    roam_og_mou_8 = request.form['roam_og_mou_8']
    loc_og_t2t_mou_8 = request.form['loc_og_t2t_mou_8']
    loc_og_t2m_mou_8 = request.form['loc_og_t2m_mou_8']
    loc_og_t2f_mou_8 = request.form['loc_og_t2f_mou_8']
    loc_og_t2c_mou_8 = request.form['loc_og_t2c_mou_8']
    std_og_t2m_mou_8 = request.form['std_og_t2m_mou_8']
    std_og_t2f_mou_8 = request.form['std_og_t2f_mou_8']
    std_og_mou_8 = request.form['std_og_mou_8']
    isd_og_mou_8 = request.form['isd_og_mou_8']
    spl_og_mou_8 = request.form['spl_og_mou_8']
    og_others_8 = request.form['og_others_8']
    total_og_mou_8 = request.form['total_og_mou_8']
    loc_ic_t2t_mou_8 = request.form['loc_ic_t2t_mou_8']
    loc_ic_t2m_mou_8 = request.form['loc_ic_t2m_mou_8']
    loc_ic_t2f_mou_8 = request.form['loc_ic_t2f_mou_8']
    std_ic_t2t_mou_8 = request.form['std_ic_t2t_mou_8']
    std_ic_t2m_mou_8 = request.form['std_ic_t2m_mou_8']
    std_ic_t2f_mou_8 = request.form['std_ic_t2f_mou_8']
    spl_ic_mou_8 = request.form['spl_ic_mou_8']
    isd_ic_mou_8 = request.form['isd_ic_mou_8']
    ic_others_8 = request.form['ic_others_8']
    total_rech_num_8 = request.form['total_rech_num_8']
    max_rech_amt_8 = request.form['max_rech_amt_8']
    last_day_rch_amt_8 = request.form['last_day_rch_amt_8']
    total_rech_data_8 = request.form['total_rech_data_8']
    max_rech_data_8 = request.form['max_rech_data_8']
    count_rech_3g_8 = request.form['count_rech_3g_8']
    av_rech_amt_data_8 = request.form['av_rech_amt_data_8']
    vol_2g_mb_8 = request.form['vol_2g_mb_8']
    vol_3g_mb_8 = request.form['vol_3g_mb_8']
    arpu_3g_8 = request.form['arpu_3g_8']
    night_pck_user_8 = request.form['night_pck_user_8']
    monthly_2g_8 = request.form['monthly_2g_8']
    fb_user_8 = request.form['fb_user_8']
    aon = request.form['aon']
    aug_vbc_3g = request.form['aug_vbc_3g']



    ''' arpu_8	onnet_mou_8	offnet_mou_8	roam_ic_mou_8	roam_og_mou_8	loc_og_t2t_mou_8	loc_og_t2m_mou_8	loc_og_t2f_mou_8	
    loc_og_t2c_mou_8	std_og_t2m_mou_8	std_og_t2f_mou_8	std_og_mou_8	isd_og_mou_8	spl_og_mou_8	
    og_others_8	total_og_mou_8	loc_ic_t2t_mou_8	loc_ic_t2m_mou_8	loc_ic_t2f_mou_8	std_ic_t2t_mou_8	
    std_ic_t2m_mou_8	std_ic_t2f_mou_8	spl_ic_mou_8	isd_ic_mou_8	ic_others_8	total_rech_num_8	
    max_rech_amt_8	last_day_rch_amt_8	total_rech_data_8	
    max_rech_data_8	count_rech_3g_8	av_rech_amt_data_8	vol_2g_mb_8	vol_3g_mb_8	arpu_3g_8	night_pck_user_8	
    monthly_2g_8	fb_user_8	aon	aug_vbc_3g
    '''
    model = pickle.load(open("rf_model_final.sav", "rb"))

    data = [[arpu_8,	onnet_mou_8,	offnet_mou_8,	roam_ic_mou_8,	roam_og_mou_8,	loc_og_t2t_mou_8,	loc_og_t2m_mou_8,	loc_og_t2f_mou_8,	
    loc_og_t2c_mou_8,	std_og_t2m_mou_8,	std_og_t2f_mou_8,	std_og_mou_8,	isd_og_mou_8,	spl_og_mou_8,	
    og_others_8,	total_og_mou_8,	loc_ic_t2t_mou_8,	loc_ic_t2m_mou_8,	loc_ic_t2f_mou_8,	std_ic_t2t_mou_8,	
    std_ic_t2m_mou_8,	std_ic_t2f_mou_8,	spl_ic_mou_8,	isd_ic_mou_8,	ic_others_8,	total_rech_num_8,
    max_rech_amt_8,	last_day_rch_amt_8,	total_rech_data_8,	
    max_rech_data_8,	count_rech_3g_8,	av_rech_amt_data_8,	vol_2g_mb_8,	vol_3g_mb_8,	arpu_3g_8,	night_pck_user_8,	
    monthly_2g_8,	fb_user_8,	aon,	aug_vbc_3g]]
    
    new_df = pd.DataFrame(data, columns = ['arpu_8',	'onnet_mou_8',	'offnet_mou_8',	'roam_ic_mou_8',	'roam_og_mou_8',	'loc_og_t2t_mou_8',	'loc_og_t2m_mou_8',	'loc_og_t2f_mou_8',	
    'loc_og_t2c_mou_8',	'std_og_t2m_mou_8',	'std_og_t2f_mou_8',	'std_og_mou_8',	'isd_og_mou_8',	'spl_og_mou_8',	
    'og_others_8',	'total_og_mou_8',	'loc_ic_t2t_mou_8',	'loc_ic_t2m_mou_8',	'loc_ic_t2f_mou_8',	'std_ic_t2t_mou_8',	
    'std_ic_t2m_mou_8',	'std_ic_t2f_mou_8',	'spl_ic_mou_8',	'isd_ic_mou_8',	'ic_others_8',	'total_rech_num_8',	
    'max_rech_amt_8',	'last_day_rch_amt_8',	'total_rech_data_8',	
    'max_rech_data_8',	'count_rech_3g_8',	'av_rech_amt_data_8',	'vol_2g_mb_8',	'vol_3g_mb_8',	'arpu_3g_8',	'night_pck_user_8',	
    'monthly_2g_8',	'fb_user_8',	'aon',	'aug_vbc_3g'])


    new_df['arpu_8'].fillna(df_1['arpu_8'].mean(), inplace=True)
    new_df['onnet_mou_8'].fillna(df_1['onnet_mou_8'].mean(), inplace=True)
    new_df['offnet_mou_8'].fillna(df_1['offnet_mou_8'].mean(), inplace=True)
    new_df['roam_ic_mou_8'].fillna(df_1['roam_ic_mou_8'].mean(), inplace=True)
    new_df['roam_og_mou_8'].fillna(df_1['roam_og_mou_8'].mean(), inplace=True)
    new_df['loc_og_t2t_mou_8'].fillna(df_1['loc_og_t2m_mou_8'].mean(), inplace=True)
    new_df['loc_og_t2m_mou_8'].fillna(df_1['loc_og_t2m_mou_8'].mean(), inplace=True)
    new_df['loc_og_t2f_mou_8'].fillna(df_1['loc_og_t2f_mou_8'].mean(), inplace=True)
    new_df['loc_og_t2c_mou_8'].fillna(df_1['loc_og_t2c_mou_8'].mean(), inplace=True)
    new_df['std_og_t2m_mou_8'].fillna(df_1['std_og_t2m_mou_8'].mean(), inplace=True)
    new_df['std_og_t2f_mou_8'].fillna(df_1['std_og_t2f_mou_8'].mean(), inplace=True)
    new_df['std_og_mou_8'].fillna(df_1['std_og_mou_8'].mean(), inplace=True)
    new_df['isd_og_mou_8'].fillna(df_1['isd_og_mou_8'].mean(), inplace=True)
    new_df['spl_og_mou_8'].fillna(df_1['spl_og_mou_8'].mean(), inplace=True)
    new_df['og_others_8'].fillna(df_1['og_others_8'].mean(), inplace=True)
    new_df['total_og_mou_8'].fillna(df_1['total_og_mou_8'].mean(), inplace=True)
    new_df['loc_ic_t2t_mou_8'].fillna(df_1['loc_ic_t2t_mou_8'].mean(), inplace=True)
    new_df['loc_ic_t2m_mou_8'].fillna(df_1['loc_ic_t2m_mou_8'].mean(), inplace=True)
    new_df['loc_ic_t2f_mou_8'].fillna(df_1['loc_ic_t2f_mou_8'].mean(), inplace=True)
    new_df['std_ic_t2t_mou_8'].fillna(df_1['std_ic_t2t_mou_8'].mean(), inplace=True)
    new_df['std_ic_t2m_mou_8'].fillna(df_1['std_ic_t2m_mou_8'].mean(), inplace=True)
    new_df['std_ic_t2f_mou_8'].fillna(df_1['std_ic_t2f_mou_8'].mean(), inplace=True)
    new_df['spl_ic_mou_8'].fillna(df_1['spl_ic_mou_8'].mean(), inplace=True)
    new_df['isd_ic_mou_8'].fillna(df_1['isd_ic_mou_8'].mean(), inplace=True)
    new_df['ic_others_8'].fillna(df_1['ic_others_8'].mean(), inplace=True)
    new_df['total_rech_num_8'].fillna(df_1['total_rech_num_8'].mean(), inplace=True)
    new_df['max_rech_amt_8'].fillna(df_1['max_rech_amt_8'].mean(), inplace=True)
    new_df['last_day_rch_amt_8'].fillna(df_1['last_day_rch_amt_8'].mean(), inplace=True)
    new_df['total_rech_data_8'].fillna(df_1['total_rech_data_8'].mean(), inplace=True)
    new_df['max_rech_data_8'].fillna(df_1['max_rech_data_8'].mean(), inplace=True)
    new_df['count_rech_3g_8'].fillna(df_1['count_rech_3g_8'].mean(), inplace=True)
    new_df['av_rech_amt_data_8'].fillna(df_1['av_rech_amt_data_8'].mean(), inplace=True)
    new_df['vol_2g_mb_8'].fillna(df_1['vol_2g_mb_8'].mean(), inplace=True)
    new_df['vol_3g_mb_8'].fillna(df_1['vol_3g_mb_8'].mean(), inplace=True)
    new_df['arpu_3g_8'].fillna(df_1['arpu_3g_8'].mean(), inplace=True)
    new_df['night_pck_user_8'].fillna(df_1['night_pck_user_8'].mean(), inplace=True)
    new_df['monthly_2g_8'].fillna(df_1['monthly_2g_8'].mean(), inplace=True)
    new_df['fb_user_8'].fillna(df_1['fb_user_8'].mean(), inplace=True)
    new_df['aon'].fillna(df_1['aon'].mean(), inplace=True)
    new_df['aug_vbc_3g'].fillna(df_1['aug_vbc_3g'].mean(), inplace=True)


    single = model.predict(new_df.tail(1))
    probablity = model.predict_proba(new_df.tail(1))
    
    if single==1:
        o1 = "This customer is likely to be churned!!"
        o2 = "Confidence: {}".format(probablity*100)
    else:
        o1 = "This customer is likely to continue!!"
        o2 = "Confidence: {}".format(probablity*100)
        
    return render_template('index.html', output1=o1, output2=o2, 
                           arpu_8 = request.form['arpu_8'],
    onnet_mou_8 = request.form['onnet_mou_8'],
    offnet_mou_8 = request.form['offnet_mou_8'],
    roam_ic_mou_8 = request.form['roam_ic_mou_8'],
    roam_og_mou_8 = request.form['roam_og_mou_8'],
    loc_og_t2t_mou_8 = request.form['loc_og_t2t_mou_8'],
    loc_og_t2m_mou_8 = request.form['loc_og_t2m_mou_8'],
    loc_og_t2f_mou_8 = request.form['loc_og_t2f_mou_8'],
    loc_og_t2c_mou_8 = request.form['loc_og_t2c_mou_8'],
    std_og_t2m_mou_8 = request.form['std_og_t2m_mou_8'],
    std_og_t2f_mou_8 = request.form['std_og_t2f_mou_8'],
    std_og_mou_8 = request.form['std_og_mou_8'],
    isd_og_mou_8 = request.form['isd_og_mou_8'],
    spl_og_mou_8 = request.form['spl_og_mou_8'],
    og_others_8 = request.form['og_others_8'],
    total_og_mou_8 = request.form['total_og_mou_8'],
    loc_ic_t2t_mou_8 = request.form['loc_ic_t2t_mou_8'],
    loc_ic_t2m_mou_8 = request.form['loc_ic_t2m_mou_8'],
    loc_ic_t2f_mou_8 = request.form['loc_ic_t2f_mou_8'],
    std_ic_t2t_mou_8 = request.form['std_ic_t2t_mou_8'],
    std_ic_t2m_mou_8 = request.form['std_ic_t2m_mou_8'],
    std_ic_t2f_mou_8 = request.form['std_ic_t2f_mou_8'],
    spl_ic_mou_8 = request.form['spl_ic_mou_8'],
    isd_ic_mou_8 = request.form['isd_ic_mou_8'],
    ic_others_8 = request.form['ic_others_8'],
    total_rech_num_8 = request.form['total_rech_num_8'],
    max_rech_amt_8 = request.form['max_rech_amt_8'],
    last_day_rch_amt_8 = request.form['last_day_rch_amt_8'],
    total_rech_data_8 = request.form['total_rech_data_8'],
    max_rech_data_8 = request.form['max_rech_data_8'],
    count_rech_3g_8 = request.form['count_rech_3g_8'],
    av_rech_amt_data_8 = request.form['av_rech_amt_data_8'],
    vol_2g_mb_8 = request.form['vol_2g_mb_8'],
    vol_3g_mb_8 = request.form['vol_3g_mb_8'],
    arpu_3g_8 = request.form['arpu_3g_8'],
    night_pck_user_8 = request.form['night_pck_user_8'],
    monthly_2g_8 = request.form['monthly_2g_8'],
    fb_user_8 = request.form['fb_user_8'],
    aon = request.form['aon'],
    aug_vbc_3g = request.form['aug_vbc_3g'])
    
app.run(debug=True)
