# (Ford go bike trip data)
## by (Mohammed A. Yassin)

## Preliminary Wrangling

> Briefly introduce your dataset here.


```python
# import all packages and set plots to be embedded inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
```

> Load in your dataset and describe its properties through the questions below.
Try and motivate your exploration goals through this section.


```python
# loading data
df = pd.read_csv('201902-fordgobike-tripdata.csv')
```


```python
# overview of the data
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>duration_sec</th>
      <th>start_time</th>
      <th>end_time</th>
      <th>start_station_id</th>
      <th>start_station_name</th>
      <th>start_station_latitude</th>
      <th>start_station_longitude</th>
      <th>end_station_id</th>
      <th>end_station_name</th>
      <th>end_station_latitude</th>
      <th>end_station_longitude</th>
      <th>bike_id</th>
      <th>user_type</th>
      <th>member_birth_year</th>
      <th>member_gender</th>
      <th>bike_share_for_all_trip</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>52185</td>
      <td>2019-02-28 17:32:10.1450</td>
      <td>2019-03-01 08:01:55.9750</td>
      <td>21.0</td>
      <td>Montgomery St BART Station (Market St at 2nd St)</td>
      <td>37.789625</td>
      <td>-122.400811</td>
      <td>13.0</td>
      <td>Commercial St at Montgomery St</td>
      <td>37.794231</td>
      <td>-122.402923</td>
      <td>4902</td>
      <td>Customer</td>
      <td>1984.0</td>
      <td>Male</td>
      <td>No</td>
    </tr>
    <tr>
      <th>1</th>
      <td>42521</td>
      <td>2019-02-28 18:53:21.7890</td>
      <td>2019-03-01 06:42:03.0560</td>
      <td>23.0</td>
      <td>The Embarcadero at Steuart St</td>
      <td>37.791464</td>
      <td>-122.391034</td>
      <td>81.0</td>
      <td>Berry St at 4th St</td>
      <td>37.775880</td>
      <td>-122.393170</td>
      <td>2535</td>
      <td>Customer</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>No</td>
    </tr>
    <tr>
      <th>2</th>
      <td>61854</td>
      <td>2019-02-28 12:13:13.2180</td>
      <td>2019-03-01 05:24:08.1460</td>
      <td>86.0</td>
      <td>Market St at Dolores St</td>
      <td>37.769305</td>
      <td>-122.426826</td>
      <td>3.0</td>
      <td>Powell St BART Station (Market St at 4th St)</td>
      <td>37.786375</td>
      <td>-122.404904</td>
      <td>5905</td>
      <td>Customer</td>
      <td>1972.0</td>
      <td>Male</td>
      <td>No</td>
    </tr>
    <tr>
      <th>3</th>
      <td>36490</td>
      <td>2019-02-28 17:54:26.0100</td>
      <td>2019-03-01 04:02:36.8420</td>
      <td>375.0</td>
      <td>Grove St at Masonic Ave</td>
      <td>37.774836</td>
      <td>-122.446546</td>
      <td>70.0</td>
      <td>Central Ave at Fell St</td>
      <td>37.773311</td>
      <td>-122.444293</td>
      <td>6638</td>
      <td>Subscriber</td>
      <td>1989.0</td>
      <td>Other</td>
      <td>No</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1585</td>
      <td>2019-02-28 23:54:18.5490</td>
      <td>2019-03-01 00:20:44.0740</td>
      <td>7.0</td>
      <td>Frank H Ogawa Plaza</td>
      <td>37.804562</td>
      <td>-122.271738</td>
      <td>222.0</td>
      <td>10th Ave at E 15th St</td>
      <td>37.792714</td>
      <td>-122.248780</td>
      <td>4898</td>
      <td>Subscriber</td>
      <td>1974.0</td>
      <td>Male</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
</div>




```python
# shape of data (rows,columns)
df.shape
```




    (183412, 16)




```python
# info about data its type 
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 183412 entries, 0 to 183411
    Data columns (total 16 columns):
     #   Column                   Non-Null Count   Dtype  
    ---  ------                   --------------   -----  
     0   duration_sec             183412 non-null  int64  
     1   start_time               183412 non-null  object 
     2   end_time                 183412 non-null  object 
     3   start_station_id         183215 non-null  float64
     4   start_station_name       183215 non-null  object 
     5   start_station_latitude   183412 non-null  float64
     6   start_station_longitude  183412 non-null  float64
     7   end_station_id           183215 non-null  float64
     8   end_station_name         183215 non-null  object 
     9   end_station_latitude     183412 non-null  float64
     10  end_station_longitude    183412 non-null  float64
     11  bike_id                  183412 non-null  int64  
     12  user_type                183412 non-null  object 
     13  member_birth_year        175147 non-null  float64
     14  member_gender            175147 non-null  object 
     15  bike_share_for_all_trip  183412 non-null  object 
    dtypes: float64(7), int64(2), object(7)
    memory usage: 22.4+ MB
    


```python
# see the statistics of data
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>duration_sec</th>
      <th>start_station_id</th>
      <th>start_station_latitude</th>
      <th>start_station_longitude</th>
      <th>end_station_id</th>
      <th>end_station_latitude</th>
      <th>end_station_longitude</th>
      <th>bike_id</th>
      <th>member_birth_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>183412.000000</td>
      <td>183215.000000</td>
      <td>183412.000000</td>
      <td>183412.000000</td>
      <td>183215.000000</td>
      <td>183412.000000</td>
      <td>183412.000000</td>
      <td>183412.000000</td>
      <td>175147.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>726.078435</td>
      <td>138.590427</td>
      <td>37.771223</td>
      <td>-122.352664</td>
      <td>136.249123</td>
      <td>37.771427</td>
      <td>-122.352250</td>
      <td>4472.906375</td>
      <td>1984.806437</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1794.389780</td>
      <td>111.778864</td>
      <td>0.099581</td>
      <td>0.117097</td>
      <td>111.515131</td>
      <td>0.099490</td>
      <td>0.116673</td>
      <td>1664.383394</td>
      <td>10.116689</td>
    </tr>
    <tr>
      <th>min</th>
      <td>61.000000</td>
      <td>3.000000</td>
      <td>37.317298</td>
      <td>-122.453704</td>
      <td>3.000000</td>
      <td>37.317298</td>
      <td>-122.453704</td>
      <td>11.000000</td>
      <td>1878.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>325.000000</td>
      <td>47.000000</td>
      <td>37.770083</td>
      <td>-122.412408</td>
      <td>44.000000</td>
      <td>37.770407</td>
      <td>-122.411726</td>
      <td>3777.000000</td>
      <td>1980.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>514.000000</td>
      <td>104.000000</td>
      <td>37.780760</td>
      <td>-122.398285</td>
      <td>100.000000</td>
      <td>37.781010</td>
      <td>-122.398279</td>
      <td>4958.000000</td>
      <td>1987.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>796.000000</td>
      <td>239.000000</td>
      <td>37.797280</td>
      <td>-122.286533</td>
      <td>235.000000</td>
      <td>37.797320</td>
      <td>-122.288045</td>
      <td>5502.000000</td>
      <td>1992.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>85444.000000</td>
      <td>398.000000</td>
      <td>37.880222</td>
      <td>-121.874119</td>
      <td>398.000000</td>
      <td>37.880222</td>
      <td>-121.874119</td>
      <td>6645.000000</td>
      <td>2001.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# making a copy
df_1= df.copy()
```


```python
# see if there's null values
df_1.isna().sum()
```




    duration_sec                  0
    start_time                    0
    end_time                      0
    start_station_id            197
    start_station_name          197
    start_station_latitude        0
    start_station_longitude       0
    end_station_id              197
    end_station_name            197
    end_station_latitude          0
    end_station_longitude         0
    bike_id                       0
    user_type                     0
    member_birth_year          8265
    member_gender              8265
    bike_share_for_all_trip       0
    dtype: int64




```python
# see if there's duplicate data
df_1.duplicated().sum()
```




    0




```python
# removing unuseful columns
df_1.drop(['start_station_id','end_station_id'],axis=1,inplace = True)
```


```python
#removing null data
df_1.dropna(inplace = True)
```


```python
# see if there's null data to make sure the previous code has worked
df_1.isna().sum()
```




    duration_sec               0
    start_time                 0
    end_time                   0
    start_station_name         0
    start_station_latitude     0
    start_station_longitude    0
    end_station_name           0
    end_station_latitude       0
    end_station_longitude      0
    bike_id                    0
    user_type                  0
    member_birth_year          0
    member_gender              0
    bike_share_for_all_trip    0
    dtype: int64




```python
# see how many bike id
df_1['bike_id'].nunique()
```




    4607




```python
#change type of start time from string to datetime
df_1['start_time']= pd.to_datetime(df['start_time'])
```


```python
# change type of end time from string to datetime
df_1['end_time']= pd.to_datetime(df['end_time'])
```


```python
# make sure of our changes
df_1.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 174952 entries, 0 to 183411
    Data columns (total 14 columns):
     #   Column                   Non-Null Count   Dtype         
    ---  ------                   --------------   -----         
     0   duration_sec             174952 non-null  int64         
     1   start_time               174952 non-null  datetime64[ns]
     2   end_time                 174952 non-null  datetime64[ns]
     3   start_station_name       174952 non-null  object        
     4   start_station_latitude   174952 non-null  float64       
     5   start_station_longitude  174952 non-null  float64       
     6   end_station_name         174952 non-null  object        
     7   end_station_latitude     174952 non-null  float64       
     8   end_station_longitude    174952 non-null  float64       
     9   bike_id                  174952 non-null  int64         
     10  user_type                174952 non-null  object        
     11  member_birth_year        174952 non-null  float64       
     12  member_gender            174952 non-null  object        
     13  bike_share_for_all_trip  174952 non-null  object        
    dtypes: datetime64[ns](2), float64(5), int64(2), object(5)
    memory usage: 20.0+ MB
    


```python
# making new column for day of week from start time 
df_1['day']= df_1['start_time'].dt.day_name()
df_1.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>duration_sec</th>
      <th>start_time</th>
      <th>end_time</th>
      <th>start_station_name</th>
      <th>start_station_latitude</th>
      <th>start_station_longitude</th>
      <th>end_station_name</th>
      <th>end_station_latitude</th>
      <th>end_station_longitude</th>
      <th>bike_id</th>
      <th>user_type</th>
      <th>member_birth_year</th>
      <th>member_gender</th>
      <th>bike_share_for_all_trip</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>52185</td>
      <td>2019-02-28 17:32:10.145</td>
      <td>2019-03-01 08:01:55.975</td>
      <td>Montgomery St BART Station (Market St at 2nd St)</td>
      <td>37.789625</td>
      <td>-122.400811</td>
      <td>Commercial St at Montgomery St</td>
      <td>37.794231</td>
      <td>-122.402923</td>
      <td>4902</td>
      <td>Customer</td>
      <td>1984.0</td>
      <td>Male</td>
      <td>No</td>
      <td>Thursday</td>
    </tr>
    <tr>
      <th>2</th>
      <td>61854</td>
      <td>2019-02-28 12:13:13.218</td>
      <td>2019-03-01 05:24:08.146</td>
      <td>Market St at Dolores St</td>
      <td>37.769305</td>
      <td>-122.426826</td>
      <td>Powell St BART Station (Market St at 4th St)</td>
      <td>37.786375</td>
      <td>-122.404904</td>
      <td>5905</td>
      <td>Customer</td>
      <td>1972.0</td>
      <td>Male</td>
      <td>No</td>
      <td>Thursday</td>
    </tr>
    <tr>
      <th>3</th>
      <td>36490</td>
      <td>2019-02-28 17:54:26.010</td>
      <td>2019-03-01 04:02:36.842</td>
      <td>Grove St at Masonic Ave</td>
      <td>37.774836</td>
      <td>-122.446546</td>
      <td>Central Ave at Fell St</td>
      <td>37.773311</td>
      <td>-122.444293</td>
      <td>6638</td>
      <td>Subscriber</td>
      <td>1989.0</td>
      <td>Other</td>
      <td>No</td>
      <td>Thursday</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1585</td>
      <td>2019-02-28 23:54:18.549</td>
      <td>2019-03-01 00:20:44.074</td>
      <td>Frank H Ogawa Plaza</td>
      <td>37.804562</td>
      <td>-122.271738</td>
      <td>10th Ave at E 15th St</td>
      <td>37.792714</td>
      <td>-122.248780</td>
      <td>4898</td>
      <td>Subscriber</td>
      <td>1974.0</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Thursday</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1793</td>
      <td>2019-02-28 23:49:58.632</td>
      <td>2019-03-01 00:19:51.760</td>
      <td>4th St at Mission Bay Blvd S</td>
      <td>37.770407</td>
      <td>-122.391198</td>
      <td>Broadway at Kearny</td>
      <td>37.798014</td>
      <td>-122.405950</td>
      <td>5200</td>
      <td>Subscriber</td>
      <td>1959.0</td>
      <td>Male</td>
      <td>No</td>
      <td>Thursday</td>
    </tr>
  </tbody>
</table>
</div>




```python
# review for our data shape
df_1.shape
```




    (174952, 15)




```python
# review for our data info
df_1.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 174952 entries, 0 to 183411
    Data columns (total 15 columns):
     #   Column                   Non-Null Count   Dtype         
    ---  ------                   --------------   -----         
     0   duration_sec             174952 non-null  int64         
     1   start_time               174952 non-null  datetime64[ns]
     2   end_time                 174952 non-null  datetime64[ns]
     3   start_station_name       174952 non-null  object        
     4   start_station_latitude   174952 non-null  float64       
     5   start_station_longitude  174952 non-null  float64       
     6   end_station_name         174952 non-null  object        
     7   end_station_latitude     174952 non-null  float64       
     8   end_station_longitude    174952 non-null  float64       
     9   bike_id                  174952 non-null  int64         
     10  user_type                174952 non-null  object        
     11  member_birth_year        174952 non-null  float64       
     12  member_gender            174952 non-null  object        
     13  bike_share_for_all_trip  174952 non-null  object        
     14  day                      174952 non-null  object        
    dtypes: datetime64[ns](2), float64(5), int64(2), object(6)
    memory usage: 21.4+ MB
    


```python
# review for our data statistics
df_1.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>duration_sec</th>
      <th>start_station_latitude</th>
      <th>start_station_longitude</th>
      <th>end_station_latitude</th>
      <th>end_station_longitude</th>
      <th>bike_id</th>
      <th>member_birth_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>174952.000000</td>
      <td>174952.000000</td>
      <td>174952.000000</td>
      <td>174952.000000</td>
      <td>174952.000000</td>
      <td>174952.000000</td>
      <td>174952.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>704.002744</td>
      <td>37.771220</td>
      <td>-122.351760</td>
      <td>37.771414</td>
      <td>-122.351335</td>
      <td>4482.587555</td>
      <td>1984.803135</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1642.204905</td>
      <td>0.100391</td>
      <td>0.117732</td>
      <td>0.100295</td>
      <td>0.117294</td>
      <td>1659.195937</td>
      <td>10.118731</td>
    </tr>
    <tr>
      <th>min</th>
      <td>61.000000</td>
      <td>37.317298</td>
      <td>-122.453704</td>
      <td>37.317298</td>
      <td>-122.453704</td>
      <td>11.000000</td>
      <td>1878.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>323.000000</td>
      <td>37.770407</td>
      <td>-122.411901</td>
      <td>37.770407</td>
      <td>-122.411647</td>
      <td>3799.000000</td>
      <td>1980.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>510.000000</td>
      <td>37.780760</td>
      <td>-122.398279</td>
      <td>37.781010</td>
      <td>-122.397437</td>
      <td>4960.000000</td>
      <td>1987.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>789.000000</td>
      <td>37.797320</td>
      <td>-122.283093</td>
      <td>37.797673</td>
      <td>-122.286533</td>
      <td>5505.000000</td>
      <td>1992.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>84548.000000</td>
      <td>37.880222</td>
      <td>-121.874119</td>
      <td>37.880222</td>
      <td>-121.874119</td>
      <td>6645.000000</td>
      <td>2001.000000</td>
    </tr>
  </tbody>
</table>
</div>



### What is the structure of your dataset?

> the data cosists of 15 columns (duration_sec,bike_id,start_time,end_time,start_station_name,start_station_latitude,start_station_longitude,end_station_name,end_station_latitude,end_station_longitude,user_type,member_birth_year,member_gender,bike_share_for_all_trip,day) and 174952 rows there are 4607 bike most variable are numeric except , start time and end time wich are time data|'start station name' ,     'end station name',day are strings| 'user type','member gender' and 'bike share for all trip' ordered variable

### What is/are the main feature(s) of interest in your dataset?

> the most interesting feature is duration of trip and its relation with day gender and user type 

### What features in the dataset do you think will help support your investigation into your feature(s) of interest?

> I think that the duration will be more in weekend (Saturday and Sunday) also I think male will have more duration trip and subscribers

## Univariate Exploration

> In this section, investigate distributions of individual variables. If
you see unusual points or outliers, take a deeper look to clean things up
and prepare yourself to look at relationships between variables.


```python
# making a countplot for the trip in each day of week 
fig, ax = plt.subplots();
color_b=sns.color_palette()[0]
order_day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
sns.countplot(data=df_1,x='day',color=color_b,order=order_day);
plt.xticks(rotation=90);
plt.xlabel('day of week')
plt.ylabel('number of ride')
plt.title('Average ride per day of the week');
```


    
![png](output_24_0.png)
    


> Unlike what I was expecting the weekend day has the lowest number of people who ride bike wich maybe due to use of bike for going to work or schools 


```python
# making a histplot for seeing distribution for duration of trips in our data
fig, ax = plt.subplots();
sns.histplot(data = df_1,x='duration_sec')
ax.set_xlim(0,5000);
plt.title('Average Trip Duration');
```


    
![png](output_26_0.png)
    


## most bike duration are arount 600-800 seconds


```python
# making a function for countplot
def countplot(d,s,a):
    sns.countplot(data=d,x=s);
    plt.title(a);
# making a count plot for trips for each gender
countplot(df_1,'member_gender','Gender')
```


    
![png](output_28_0.png)
    


#### As I expected male will be more the female 


```python
# making a count plot for trips for each user type
countplot(df_1,"user_type","User Type")
```


    
![png](output_30_0.png)
    


#### As I expected subscriber will be more the customer

### Discuss the distribution(s) of your variable(s) of interest. Were there any unusual points? Did you need to perform any transformations?

> most of distribution goes as I expected except for the days of the week which has shown that the weekend has the lowest number of ride , Also the duration of trip was between 600- 800 second ie 10-13 min which indicates that most trip maybe to near workplace or schools 

### Of the features you investigated, were there any unusual distributions? Did you perform any operations on the data to tidy, adjust, or change the form of the data? If so, why did you do this?

> no the data were tidy as I have already wrangled it before visualization

## Bivariate Exploration

> In this section, investigate relationships between pairs of variables in your
data. Make sure the variables that you cover here have been introduced in some
fashion in the previous section (univariate exploration).


```python
# making a boxplot to see the relation and distribution for trip duration and each day of the week
fig, ax = plt.subplots();
sns.boxplot(data=df_1,x='day',y='duration_sec')
plt.xticks(rotation=90);
plt.title('duration of trip for each week');
```




    Text(0.5, 1.0, 'duration of trip for each week')




    
![png](output_34_1.png)
    


#### intrestingly Saturday and Sunday has the heighst duration for trip although in lower duration they're the lowest as in holiday people go biking for entertainment or sport not for going work or school (which is usually will be near otherwise they'll use public transport :) )


```python
# making a bar plot to see the relation and distribution for trip duration and each Gender
fig, ax = plt.subplots();
sns.barplot(data=df_1,x='member_gender',y='duration_sec')
plt.xticks(rotation=90);
plt.title('relation for duration of trip and each gender')
```




    Text(0.5, 1.0, 'relation for duration of trip and each gender')




    
![png](output_36_1.png)
    


#### interstingly male has the lowest duration for trip than female or others (males are lazier :) ) 


```python
# making a bar to see the relation and distribution for trip duration and each user type
fig, ax = plt.subplots();
sns.barplot(data=df_1,x='user_type',y='duration_sec')
plt.xticks(rotation=90);
plt.title('relation for duration of trip and each User Type');
```




    Text(0.5, 1.0, 'relation for duration of trip and each User Type')




    
![png](output_38_1.png)
    


#### interstingly the customer has much more duration for trip than subscriber (which also indicate that subscriber usually person going to workplace rather than customer who just use it for sporting or entertainment

### Talk about some of the relationships you observed in this part of the investigation. How did the feature(s) of interest vary with other features in the dataset?

> Although male has much number of ride than female or other but they have the lowest duration which maybe that male use bike more for routine (going work or school) rather than use it for entertainment or sporting , also the day of the week show the same effect which indicate that the duration of ride increases more when riding the bike as a hobby rather than routine activities 



## Multivariate Exploration

> Create plots of three or more variables to investigate your data even
further. Make sure that your investigations are justified, and follow from
your work in the previous sections.


```python
# making a violin plot to see the relation and distribution for trip duration day of week and each gender
fig, ax = plt.subplots(figsize=(10,10));
sns.violinplot(data=df_1,x='day',y='duration_sec',hue='member_gender')
plt.xticks(rotation=90);
plt.title('relation for duration of trip ,day of week and each gender')
plt.legend();
```


    
![png](output_42_0.png)
    



```python
# making a violin plot to see the relation and distribution for trip duration day of week and each user type
fig, ax = plt.subplots(figsize=(10,10));
sns.violinplot(data=df_1,x='day',y='duration_sec',hue='user_type')
plt.xticks(rotation=90);
plt.title('relation for duration of trip ,day of week and each user type')
plt.legend();
```


    
![png](output_43_0.png)
    


### Talk about some of the relationships you observed in this part of the investigation. Were there features that strengthened each other in terms of looking at your feature(s) of interest?

> from the 2 visualization we see that male are much more in the whole week but more from Monday to Friday while Female and others have much more trip in the weekend also we can see that the relaton between trip duration is more with others then Female then Male , the same thing is seen with relation between subscribers customers and trip duration although subscriber have much more trip than customers but customers tend to have much trip duration especially in the weekend

### Were there any interesting or surprising interactions between features?

> the intersting relationship -which further investigation by gathering more data for the whole year and many years- is that the reason why riding the bike affect the trip duration so if you you routinley ride bicycle your number of trip will increase but the duration of trip will be less 

> At the end of your report, make sure that you export the notebook as an
html file from the `File > Download as... > HTML` menu. Make sure you keep
track of where the exported file goes, so you can put it in the same folder
as this notebook for project submission. Also, make sure you remove all of
the quote-formatted guide notes like this one before you finish your report!


```python

```
