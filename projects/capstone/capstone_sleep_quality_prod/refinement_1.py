import train_and_test
from lib.results_handler import generate_results,summurize_results,showing_mean_values

#Getting final inputs and a target variable
features_final, target_var= train_and_test.get_feature_final_and_target_var()

# Specifying information of the result I want.
result_keys = [
            'random_state',
            'base_clf_f1_score',
            'base_clf_n_estimators',
            'best_clf_f1_score',
            'best_clf_n_estimators',
            'best_clf_learning_rate',
            'time'
        ]

# Specifying arguments of the method  except for random_state
other_args = {
    'features_final': features_final,
    'target_var': target_var,
    'f_select_range':[]
}

#Specifying random_states
random_states = range(1)

#Executing training and testing 10 times with 10 different inputs and getting the results
all_res_df = generate_results(train_and_test, 'train_and_measure_performance_1', result_keys, random_states, other_args)

#Preparation for making a summary for the results
result_keys.remove('random_state')
summary_config = {}
for result_column in result_keys:
    summary_config[result_column] = 'mean'

#Combining the result and summary and outputting it to csv
summary_df = summurize_results(all_res_df,summary_config)
all_res_df_with_summary = all_res_df.append(summary_df,ignore_index=True)
all_res_df_with_summary.to_csv("results_rf_arf.csv")

#Printing the results
print all_res_df_with_summary
showing_mean_values(all_res_df, result_keys)