{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "29e63fd4-b734-4d56-afe2-76e93fe487c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-06 10:08:51.438 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\bhava\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-04-06 10:08:51.438 Session state does not function when running a script without `streamlit run`\n"
     ]
    },
    {
     "ename": "StreamlitAPIException",
     "evalue": "Slider value should either be an int/float/datetime or a list/tuple of 0 to 2 ints/floats/datetimes",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mStreamlitAPIException\u001b[0m                     Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[4], line 20\u001b[0m\n\u001b[0;32m     18\u001b[0m payment_delay \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39mslider(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPayment Delay (days)\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m60\u001b[39m, \u001b[38;5;241m5\u001b[39m)\n\u001b[0;32m     19\u001b[0m subscription_type \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39mselectbox(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSubscription Type\u001b[39m\u001b[38;5;124m\"\u001b[39m, [\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBasic\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mStandard\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mPremium\u001b[39m\u001b[38;5;124m'\u001b[39m])\n\u001b[1;32m---> 20\u001b[0m contract_length \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39mslider(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mContract Length\u001b[39m\u001b[38;5;124m\"\u001b[39m, [\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mMonthly\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mQuarterly\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mAnnual\u001b[39m\u001b[38;5;124m'\u001b[39m])\n\u001b[0;32m     21\u001b[0m total_spend \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39mnumber_input(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTotal Spend\u001b[39m\u001b[38;5;124m\"\u001b[39m, min_value\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0.0\u001b[39m, step\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m10.0\u001b[39m)\n\u001b[0;32m     22\u001b[0m last_interaction \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39mslider(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLast Interaction (days ago)\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m365\u001b[39m, \u001b[38;5;241m30\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\metrics_util.py:408\u001b[0m, in \u001b[0;36mgather_metrics.<locals>.wrapped_func\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    406\u001b[0m         _LOGGER\u001b[38;5;241m.\u001b[39mdebug(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFailed to collect command telemetry\u001b[39m\u001b[38;5;124m\"\u001b[39m, exc_info\u001b[38;5;241m=\u001b[39mex)\n\u001b[0;32m    407\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 408\u001b[0m     result \u001b[38;5;241m=\u001b[39m non_optional_func(\u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n\u001b[0;32m    409\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m RerunException \u001b[38;5;28;01mas\u001b[39;00m ex:\n\u001b[0;32m    410\u001b[0m     \u001b[38;5;66;03m# Duplicated from below, because static analysis tools get confused\u001b[39;00m\n\u001b[0;32m    411\u001b[0m     \u001b[38;5;66;03m# by deferring the rethrow.\u001b[39;00m\n\u001b[0;32m    412\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m tracking_activated \u001b[38;5;129;01mand\u001b[39;00m command_telemetry:\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\streamlit\\elements\\widgets\\slider.py:340\u001b[0m, in \u001b[0;36mSliderMixin.slider\u001b[1;34m(self, label, min_value, max_value, value, step, format, key, help, on_change, args, kwargs, disabled, label_visibility)\u001b[0m\n\u001b[0;32m    192\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124mr\u001b[39m\u001b[38;5;124;03m\"\"\"Display a slider widget.\u001b[39;00m\n\u001b[0;32m    193\u001b[0m \n\u001b[0;32m    194\u001b[0m \u001b[38;5;124;03mThis supports int, float, date, time, and datetime types.\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    337\u001b[0m \n\u001b[0;32m    338\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    339\u001b[0m ctx \u001b[38;5;241m=\u001b[39m get_script_run_ctx()\n\u001b[1;32m--> 340\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_slider(\n\u001b[0;32m    341\u001b[0m     label\u001b[38;5;241m=\u001b[39mlabel,\n\u001b[0;32m    342\u001b[0m     min_value\u001b[38;5;241m=\u001b[39mmin_value,\n\u001b[0;32m    343\u001b[0m     max_value\u001b[38;5;241m=\u001b[39mmax_value,\n\u001b[0;32m    344\u001b[0m     value\u001b[38;5;241m=\u001b[39mvalue,\n\u001b[0;32m    345\u001b[0m     step\u001b[38;5;241m=\u001b[39mstep,\n\u001b[0;32m    346\u001b[0m     \u001b[38;5;28mformat\u001b[39m\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mformat\u001b[39m,\n\u001b[0;32m    347\u001b[0m     key\u001b[38;5;241m=\u001b[39mkey,\n\u001b[0;32m    348\u001b[0m     help\u001b[38;5;241m=\u001b[39mhelp,\n\u001b[0;32m    349\u001b[0m     on_change\u001b[38;5;241m=\u001b[39mon_change,\n\u001b[0;32m    350\u001b[0m     args\u001b[38;5;241m=\u001b[39margs,\n\u001b[0;32m    351\u001b[0m     kwargs\u001b[38;5;241m=\u001b[39mkwargs,\n\u001b[0;32m    352\u001b[0m     disabled\u001b[38;5;241m=\u001b[39mdisabled,\n\u001b[0;32m    353\u001b[0m     label_visibility\u001b[38;5;241m=\u001b[39mlabel_visibility,\n\u001b[0;32m    354\u001b[0m     ctx\u001b[38;5;241m=\u001b[39mctx,\n\u001b[0;32m    355\u001b[0m )\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\streamlit\\elements\\widgets\\slider.py:434\u001b[0m, in \u001b[0;36mSliderMixin._slider\u001b[1;34m(self, label, min_value, max_value, value, step, format, key, help, on_change, args, kwargs, disabled, label_visibility, ctx)\u001b[0m\n\u001b[0;32m    432\u001b[0m range_value \u001b[38;5;241m=\u001b[39m \u001b[38;5;28misinstance\u001b[39m(value, (\u001b[38;5;28mlist\u001b[39m, \u001b[38;5;28mtuple\u001b[39m)) \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(value) \u001b[38;5;129;01min\u001b[39;00m (\u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m)\n\u001b[0;32m    433\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m single_value \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m range_value:\n\u001b[1;32m--> 434\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StreamlitAPIException(\n\u001b[0;32m    435\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSlider value should either be an int/float/datetime or a list/tuple of \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    436\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m0 to 2 ints/floats/datetimes\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    437\u001b[0m     )\n\u001b[0;32m    439\u001b[0m \u001b[38;5;66;03m# Simplify future logic by always making value a list\u001b[39;00m\n\u001b[0;32m    440\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m single_value:\n",
      "\u001b[1;31mStreamlitAPIException\u001b[0m: Slider value should either be an int/float/datetime or a list/tuple of 0 to 2 ints/floats/datetimes"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import pickle\n",
    "\n",
    "# Load trained model and scaler\n",
    "model = pickle.load(open('rf_model.pkl', 'rb'))\n",
    "#scaler = pickle.load(open('scaler.pkl', 'rb'))  # if used\n",
    "\n",
    "st.title(\"Churn Prediction App\")\n",
    "\n",
    "# UI inputs (match these to your dataset features)\n",
    "age = st.slider(\"Age\", 18, 100, 30)\n",
    "gender = st.selectbox(\"Gender\", ['Male', 'Female'])\n",
    "tenure = st.slider(\"Tenure\", 0, 72, 12)\n",
    "usage_freq = st.slider(\"Usage Frequency\", 0, 100, 20)\n",
    "support_calls = st.slider(\"Support Calls\", 0, 30, 2)\n",
    "payment_delay = st.slider(\"Payment Delay (days)\", 0, 60, 5)\n",
    "subscription_type = st.selectbox(\"Subscription Type\", ['Basic', 'Standard', 'Premium'])\n",
    "contract_length = st.selectbox(\"Contract Length\", ['Monthly', 'Quarterly', 'Annual'])\n",
    "total_spend = st.number_input(\"Total Spend\", min_value=0.0, step=10.0)\n",
    "last_interaction = st.slider(\"Last Interaction (days ago)\", 0, 365, 30)\n",
    "\n",
    "# Encode values like you did in training\n",
    "gender = 1 if gender == 'Male' else 0\n",
    "subscription_map = {'Basic': 0, 'Standard': 1, 'Premium': 2}\n",
    "subscription_type = subscription_map[subscription_type]\n",
    "contract_length_map = {'Monthly': 0, 'Quarterly': 1, 'Annual': 2}\n",
    "contract_length = contract_length_map[contract_length]\n",
    "\n",
    "# Create a DataFrame for prediction\n",
    "input_df = pd.DataFrame([[age, gender, tenure, usage_freq, support_calls, payment_delay,\n",
    "                          subscription_type, contract_length, total_spend, last_interaction]],\n",
    "                        columns=['Age', 'Gender', 'Tenure', 'Usage Frequency', 'Support Calls',\n",
    "                                 'Payment Delay', 'Subscription Type', 'Contract Length',\n",
    "                                 'Total Spend', 'Last Interaction'])\n",
    "\n",
    "# Scale if necessary\n",
    "if scaler:\n",
    "    input_df = scaler.transform(input_df)\n",
    "\n",
    "# Predict\n",
    "pred = model.predict(input_df)[0]\n",
    "prob = model.predict_proba(input_df)[0][1]\n",
    "\n",
    "st.subheader(\"Prediction Result:\")\n",
    "if pred == 1:\n",
    "    st.error(f\"⚠️ Customer likely to churn (probability: {prob:.2f})\")\n",
    "else:\n",
    "    st.success(f\"✅ Customer likely to stay (probability: {prob:.2f})\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
