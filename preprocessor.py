# import re
# import pandas as pd

# def preprocess(data):
#     pattern = r'\[\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}:\d{2}\s[APap][mM]\]\s'

#     messages = re.split(pattern, data)[1:] 
#     dates = re.findall(pattern, data)

#     if len(messages) != len(dates):
#         print("Warning: Mismatch in lengths of messages and dates. Adjusting to the minimum length.")
#         min_length = min(len(messages), len(dates))
#         messages = messages[:min_length]
#         dates = dates[:min_length]

#     dates_cleaned = [date.strip(' []') for date in dates] 

#     df = pd.DataFrame({'user_message': messages, 'message_date': dates_cleaned})

#     df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M:%S %p', errors='coerce')

#     df.rename(columns={'message_date': 'date'}, inplace=True)

#     users = []
#     messages = []
#     for message in df['user_message']:
#         entry = re.split(r'([\w\W]+?):\s', message)
#         if entry[1:]: 
#             users.append(entry[1])
#             messages.append(" ".join(entry[2:]))
#         else:
#             users.append('group_notification')
#             messages.append(entry[0])

#     df['user'] = users
#     df['message'] = messages
#     df.drop(columns=['user_message'], inplace=True)

#     df = df[df['user'] != 'group_notification']

#     df['only_date'] = df['date'].dt.date
#     df['year'] = df['date'].dt.year
#     df['month_num'] = df['date'].dt.month
#     df['month'] = df['date'].dt.month_name()
#     df['day'] = df['date'].dt.day
#     df['day_name'] = df['date'].dt.day_name()
#     df['hour'] = df['date'].dt.hour
#     df['minute'] = df['date'].dt.minute

#     period = []
#     for hour in df['hour']:
#         if hour == 23:
#             period.append(f"{hour}-00")
#         elif hour == 0:
#             period.append(f"00-{hour + 1}")
#         else:
#             period.append(f"{hour}-{hour + 1}")

#     df['period'] = period

#     return df
import re
import pandas as pd

def preprocess(data):
    pattern = r'\[\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}:\d{2}\s[APap][mM]\]\s'

    messages = re.split(pattern, data)[1:] 
    dates = re.findall(pattern, data)

    if len(messages) != len(dates):
        print("Warning: Mismatch in lengths of messages and dates. Adjusting to the minimum length.")
        min_length = min(len(messages), len(dates))
        messages = messages[:min_length]
        dates = dates[:min_length]

    dates_cleaned = [date.strip(' []') for date in dates] 

    df = pd.DataFrame({'user_message': messages, 'message_date': dates_cleaned})

    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M:%S %p', errors='coerce')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)
        if entry[1:]: 
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    # Filter out messages containing certain keywords
    keywords_to_exclude = ['document', 'image', 'omitted']
    df = df[~df['message'].str.contains('|'.join(keywords_to_exclude), case=False, na=False)]

    df = df[df['user'] != 'group_notification']

    # Calculate total words
    total_words = df['message'].str.split().map(len).sum()

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append(f"{hour}-00")
        elif hour == 0:
            period.append(f"00-{hour + 1}")
        else:
            period.append(f"{hour}-{hour + 1}")

    df['period'] = period

    return df, total_words
