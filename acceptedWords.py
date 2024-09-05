ocr_to_accepted_words = {
    # "秩父の天然水": {'秩父の天然水', '父の天然水', '稚父の天然水', '种父の天然水',
    #                  '地父の天然水', '稚父の天然木', '地父の天然木', '秩父の天然'},
    "ラミックス": {'ラミックス', 'ラミツクス', 'ラミッス', 'ラミッウス', 'ラミッケス', 'ラミック'},

    "ラミックス2": {'ラミックス2', 'ラミツクス2', 'ラミッス2', 'ラミッウス2', 'ラミッケス2'},
    "ラミックス静岡": {'ラミックス静岡', 'ラミツクス静岡', 'ラミッス静岡', 'ラミッウス静岡', 'ラミッケス静岡',
                       'ラミックス静田', 'ラミックス静国'},
    "ラミックス群馬": {'ラミックス群馬', 'ラミツクス群馬', 'ラミッス群馬', 'ラミッウス群馬', 'ラミッケス群馬',
                       'ラミックス鮮馬', 'ラミックス群店', 'ラミックス群居', 'ラミックス群用', 'ラミックス洋馬'},
    "ラミックス湘南": {'ラミックス湘南', 'ラミツクス湘南', 'ラミッス湘南', 'ラミッウス湘南', 'ラミッケス湘南'},
    "ラミックス厚木１": {'ラミックス厚木1', 'ラミツクス厚木1', 'ラミッス厚木1', 'ラミッウス厚木1', 'ラミッケス厚木1',
                        'フミックス原木1'},
    "ラミックス厚木２": {'ラミックス厚木2', 'ラミツクス厚木2', 'ラミッス厚木2', 'ラミッウス厚木2', 'ラミッケス厚木2',
                        'フミックス原木2'},
    "ラミックス横浜２": {'ラミックス横浜2', 'ラミツクス横浜2', 'ラミッス横浜2', 'ラミッウス横浜2', 'ラミッケス横浜2'},
    "ラミックス川崎": {'ラミックス川崎', 'ラミツクス川崎', 'ラミッス川崎', 'ラミッウス川崎', 'ラミッケス川崎',
                       'ラミッケ久川崎'},

    "アブロード横浜": {'アブロード横浜', 'アプロド横浜', 'アプロ一ド横浜', 'アブロ一ド横浜', 'アブロード浜',
                       'アブロード横', 'ド横浜'},
    "アブロード杉並府中": {'アブロード杉並府中', 'アプロ一ド杉並府中', 'アブロ一ド杉並府中', 'アプロ一ード杉並府中',
                           'アブロード杉並府'},
    "アブロード銀座": {'アブロード銀座', 'アプロード銀座', 'アプロ一ド銀座', 'アプロ一ド銀産', 'アブロ一ド銀座',
                       'アプロ一ード銀座', 'アプロード銀', 'アヴロード銀', 'ド銀座'},
    "アブロード多摩": {'アブロード多摩', 'アブロ一ド多摩', 'アプロード多摩', 'アプロ一ド多摩', 'アプロ一ド多時',
                       'アプロ一ド多曜', 'アプロード多店', 'アデロード多摩',
                       'アブロ一ド多席', 'アプロ一ド多席', 'アプロード多麻', 'アブロ一ド多産', 'アプロ一ド多産',
                       'アブロ一ド多座', 'アプロ一ド多座', 'アプロ一ド多町', 'アプロ一ド多度', 'アプロー一ド多産',
                       'アブロ一ド多庫', 'アプロ一ド多庫', 'アプロ一ド多駐', 'アプロ一ド多麻', 'アブロ一ド多曜',
                       'アブロ一ド多', 'アプロ一ド多', 'アプロード多庫', 'アブロード多度', 'アプロード多席'},
    "アブロード北東京": {'アブロード北東京', 'アプロ一ド北東京', 'アプロード北東京', 'アブロ一ド北東京',
                         'アプロ一一ド北東京', 'ド北東京'},
    "アブロード新宿": {'アブロード新宿', 'アプロード新宿', 'アプロ一ド新宿', 'アブロ一ド新宿', 'ド新宿', 'ロード新宿'},
    "アブロード戸田": {'アブロード戸田', 'アプロ一ド戸田', 'アブロ一ド戸田', 'ド戸田'},
    "アブロード北東京新宿": {'アブロード北東京新宿', 'アプロ一ド北東京新宿', 'アブロ一ド北東京新宿', 'ド北東京新宿'},
    "アブロード千葉": {'アブロード千葉', 'アプロ一ド千葉', 'アブロ一ド千葉', 'アプロード千葉', 'アプロ一ドモ葉',
                       'アブロード干葉'},

    "ムロオ共配": {'ムロオ共配', 'ム日オ共配', 'ムロオ共国', 'ムロオ共起'},
    "ムロオ北東京２": {'ムロオ北東京2', 'ム日オ北東京2', 'ム日オヒ東京2'},

    "柏倉庫(引取り)": {'柏倉庫(引取り)', '柏倉庫(取り)', '柏倉庫(引取', '柏倉庫(号取り)', '拍倉座(取り)',
                       '柏倉車(5取り)',
                       '拍倉庫(号取り)', '柏倉庫(3取り)', '柏倉庫(ら取り)', '泊倉庫(引取り)', '旧倉庫(引取り)',
                       '柏倉庫(5取り', '拍倉庫(弓取り)', '拍倉庫(取り)', '倉庫(引取り)'},
    "来　社": {'来社'},
    "西濃": {'西濃', '西縄', '西麗', '西潤'}

}
