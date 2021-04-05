from csv import reader
import matplotlib.pyplot as plt
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

fb_rating_data = [row_1[0], row_1[3], row_1[-1]]
insta_rating_data = [row_2[0], row_2[3], row_2[4]]
pandora_rating_data = [row_5[0], row_5[3], row_5[4]]

avg_rating = (fb_rating_data[2] + insta_rating_data[2] +
              pandora_rating_data[2]) / 3
print(avg_rating)
print(row_3[-3:])

# List in a List
data_set = [row_1, row_2, row_3, row_4, row_5]
print(data_set)

print(data_set[2][-1])

fb_row = data_set[1]
print(fb_row)
print(fb_row[-1])

app_data_set = [row_1, row_2, row_3, row_4, row_5]

avg_one = app_data_set[0][-1]
avg_two = app_data_set[1][-1]
avg_three = app_data_set[2][-1]
avg_four = app_data_set[3][-1]
avg_five = app_data_set[4][-1]

avg_rating = (avg_one + avg_two + avg_three + avg_four + avg_five) / 5
print(avg_rating)
print('ernest lipson'.title())

for e in app_data_set:
    print(e)
# printing the last elements of each list
for each in app_data_set:
    rating = each[-1]
    print(rating)

rating_sum = 0
for row in app_data_set:
    rating = row[-1]
    rating_sum = rating_sum + rating
    print(rating_sum)

avg_rating = rating_sum / len(app_data_set)
print(avg_rating)

open_file = open('1000 Sales Records.csv')
print(open_file)

read_file = reader(open_file)
apps_data = list(read_file)
print(len(apps_data))
print(apps_data[:5])
# looping through the created  list
for row in apps_data[1:]:   # this slice excludes the column header
    print(row)

print(rating_sum)

# calculating the average rating of AppleStore
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum = 0
for row in apps_data[1:]:   # this slice excludes the column header
    rating = float(row[7])
    rating_sum = rating_sum + rating

avg_rating = rating_sum / 7197

print(f'\n{avg_rating}')

# alternative method to calculating avg rating
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

all_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    all_ratings.append(rating)

avg_rating = sum(all_ratings) / len(all_ratings)
print(avg_rating)
