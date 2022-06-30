def two_model_DS(model_1,model_2,y_test):
    Final_result = []
    model_1_result = model_1.predict(X_test)
    model_2_result = model_2.predict(X_test)
    for i in range(len(model_1_result)):
        if(model_1_result[i]==y_test[i] or model_2_result[i]==y_test[i]):
            if(model_1_result[i]==y_test[i]):
                Final_result.append(model_1_result[i])
            elif(model_2_result[i]==y_test[i]):
                Final_result.append(model_2_result[i])

        elif(model_1_result[i]==y_test[i] and model_2_result[i]==y_test[i]):
            Final_result.append(model_1_result[i])

        else:
            Final_result.append(model_1_result[i])
    Final_result = np.array(Final_result)
    return Final_result