import joblib
import numpy
university_name = ['northeastern_university',
    #    'clemson_university', 
    #    'george_mason_university',
    #    'carnegie_mellon_university'
       'georgia_institiute_of_technology',
       'illinois_institute_of_technology',
       'indiana_university_bloomington', 'kansas_state_university',
       'university_of_maryland_college_park',
       'michigan_technological_university',
       'north_carolina_state_university_raleigh', 'new_york_university',
       'rochester_institute_of_technology',
       'rutgers_university_new_brunswick',
       'state_university_of_new_york_at_stony_brook',
       'syracuse_university', 'texas_a_m_university_college_station',
       'university_of_connecticut', 'university_of_colorado_boulder',
       'university_of_california_irvine', 'university_of_florida',
       'university_of_north_carolina_at_charlotte',
       'university_of_southern_california',
       'university_of_texas_arlington', 'university_of_texas_austin',
       'university_of_texas_dallas', 'university_of_iowa',
       'university_of_cincinnati', 'worcester_polytechnic_institute']

# avg_gre={
#     "northeastern_university" :313.7142857142857,
# "clemson_university" :309.4725274725275,
# "george_mason_university" :307.6212121212121,
# "georgia_institiute_of_technology" :324.9894736842105,
# "illinois_institute_of_technology" :306.57055214723925,
# "kansas_state_university" :309.5964912280702,
# "north_carolina_state_university_raleigh" :318.74603174603175,
# "new_york_university" :318.5504201680672,
# "rochester_institute_of_technology":309.1843137254902,
# "rutgers_university_new_brunswick" :318.6140350877193,
# "state_university_of_new_york_at_stony_brook" :318.61862527716187,
# "syracuse_university" :310.1159793814433,
# "texas_a_m_university_college_station" :320.5896551724138,
# "university_of_connecticut" :310.3958333333333,
# "university_of_colorado_boulder" :316.61960784313726,
# 'university_of_florida' :316.15492957746477,
# "university_of_north_carolina_at_charlotte" :307.29122807017546,
# 'university_of_texas_arlington' :303.7735042735043,
# 'university_of_texas_dallas' :312.4478873239437,
# 'worcester_polytechnic_institute' :310.3269230769231 
# }

avg_gre={
    "northeastern_university": 315.9094076655052,
"clemson_university": 308.6463414634146,
"george_mason_university": 308.6607142857143,
"georgia_institiute_of_technology" :324.81609195402297,
"illinois_institute_of_technology": 307.3768656716418,
"kansas_state_university" :311.29545454545456,
"north_carolina_state_university_raleigh": 321.19572953736656,
"new_york_university":319.8776978417266,
"rochester_institute_of_technology": 312.3645320197044,
"rutgers_university_new_brunswick": 320.5925925925926,
"state_university_of_new_york_at_stony_brook": 320.5053380782918,
"syracuse_university" :311.34033613445376,
"texas_a_m_university_college_station": 322.9698795180723,
"university_of_connecticut": 311.5263157894737,
"university_of_colorado_boulder": 318.16438356164383,
"university_of_florida": 318.0833333333333,
"university_of_north_carolina_at_charlotte": 307.9135135135135,
"university_of_texas_arlington": 305.12359550561797,
"university_of_texas_dallas" :315.56768558951967,   
"worcester_polytechnic_institute": 312.2121212121212 
}

toefl = {
    "northeastern_university": 103.39198606271778,
"clemson_university": 91.63414634146342,
"george_mason_university": 96.39880952380952,
"georgia_institiute_of_technology" :106.36781609195403,
"illinois_institute_of_technology": 89.43283582089552,
"kansas_state_university" :95.04545454545455,
"north_carolina_state_university_raleigh": 102.64768683274022,
"new_york_university": 99.73381294964028,
"rochester_institute_of_technology": 96.67487684729063,
"rutgers_university_new_brunswick": 103.23148148148148,
"state_university_of_new_york_at_stony_brook": 103.96797153024912,
"syracuse_university" :95.23529411764706,
"texas_a_m_university_college_station": 102.76506024096386,
"university_of_connecticut" :94.94736842105263,
"university_of_colorado_boulder": 103.86301369863014,
"university_of_florida": 106.48333333333333,
"university_of_north_carolina_at_charlotte" :94.0972972972973,
"university_of_texas_arlington": 91.15730337078652,
"university_of_texas_dallas": 101.73799126637554,
"worcester_polytechnic_institute": 100.54545454545455 
}

def general_results(gre, gre_quants, gre_verbal, ug_cgpa, toefl, no_of_papers, work_experience):
    arr = []
    for university in university_name:
        loaded_model = joblib.load("./pickle_files/"+university+".pickel")
        # print(university+" "+loaded_model.predict([[0.0, 0.0,  0.0,0.0,0.0,0.0,0.0]]))
        a = (university+" "+loaded_model.predict([[gre, gre_quants, gre_verbal, ug_cgpa, toefl, no_of_papers, work_experience]]))
        print(','.join(str(x) for x in a))
        if((','.join(str(x) for x in a).split())[-1]=='accept') and gre!=0 and toefl!=0:
            arr.append(university)
        else:
            pass
    return arr

def college_based(gre, gre_quants, gre_verbal, ug_cgpa, toefl, no_of_papers, work_experience, university):
    loaded_model = joblib.load("./pickle_files/"+university+".pickel")
    a = (university+" "+loaded_model.predict([[gre, gre_quants, gre_verbal, ug_cgpa, toefl, no_of_papers, work_experience]]))
    return (','.join(str(x) for x in a).split())[-1]=='accept'