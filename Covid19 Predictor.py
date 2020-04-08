


import pandas as pd
import numpy as np
import pickle


# In[7]:


df = pd.read_csv(r'C:\Users\vividha\Desktop\Datasets\covid19 dataset\Cleaned-Data.csv')
df.tail()


# In[10]:




# In[16]:


df.shape


# In[45]:




# In[20]:


df.dtypes


# In[24]:


df['Severity'] = (df.iloc[:, 19:23] == 1).idxmax(1)


# In[27]:


df.head()


# In[31]:


df['Severity'].value_counts()


# In[165]:


df['Target'] = df['Severity'].replace('Severity_None', 0).replace('Severity_Mild', 1).replace('Severity_Moderate', 1).replace('Severity_Severe', 1)


# In[140]:


df.tail()


# In[166]:


df.iloc[:, 23:26].head()


# In[167]:


df['Contact'] = (df.iloc[:, 23:26] == 1).idxmax(1)


# In[168]:


df.head()


# In[169]:


df['Contact'].value_counts()


# In[170]:


df['Contact'] = df['Contact'].replace('Contact_No', 0).replace('Contact_Yes', 1).replace('Contact_Dont-Know', 2)


# In[171]:


df.head()


# In[172]:


df.dtypes


# In[173]:


df.iloc[:, 11:16].head()


# In[174]:


df['Age_Label'] = (df.iloc[:, 11:16] == 1).idxmax(1)
df['Age_Label'] = df['Age_Label'].replace('Age_0-9', 0).replace('Age_10-19', 1).replace('Age_20-24', 2).replace('Age_25-59', 3).replace('Age_60+', 4)


# In[175]:


df.tail()


# In[176]:


df.iloc[:, 16:19].head()


# In[177]:


df['Gender'] = (df.iloc[:, 16:19] == 1).idxmax(1)
df['Gender'] = df['Gender'].replace('Gender_Female', 1).replace('Gender_Male', 0).replace('Gender_Transgender', 2)


# In[151]:


df.head()


# In[178]:


df.columns


# In[162]:


X = df[['Fever', 'Tiredness', 'Dry-Cough', 'Difficulty-in-Breathing',
       'Sore-Throat', 'Pains', 'Nasal-Congestion',
       'Runny-Nose', 'Diarrhea', 'Contact', 'Age_Label',
       'Gender']]
X.head()


# In[179]:


Y = df[['Target']]
Y.head()


# In[180]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 4)
x_train.shape, y_train.shape


# In[181]:


from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
LR.fit(x_train, y_train)


# In[182]:


y_pred = LR.predict(x_test)


# In[184]:


import sklearn.metrics as skm
skm.multilabel_confusion_matrix(y_test, y_pred)


# In[185]:


print(skm.classification_report(y_test, y_pred))

pickle.dump(LR, open('ml.pkl', 'wb'))

ml = pickle.load(open('ml.pkl', 'rb'))


