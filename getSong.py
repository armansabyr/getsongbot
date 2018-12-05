import requests
import telebot
from telebot import types
import bs4
from bs4 import BeautifulSoup




bot = telebot.TeleBot("624075515:AAE-3_E0Jw5iCPDaCXksUna4eMTcSZtvksc")

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
	print(message)
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=["text"])
def send_message(message):
	#print(message.text)
	#bot.send_message(message.chat.id, "ya poimal message")
# while 1:
	# song = input("Enter a lyric: ")
	url = "https://genius.com/api/search/multi?q=" + message.text
	print(url)
	res = requests.get(url)
	print(res.json()['response']['sections'][0])
	# try:
		# itembtn1 = bot.send_message(message.chat.id, res.json()['response']['sections'][0]['hits'][0]['result']['full_title'])
		# itembtn2 = bot.send_message(message.chat.id, res.json()['response']['sections'][0]['hits'][1]['result']['full_title'])
		# itembtn3 = bot.send_message(message.chat.id, res.json()['response']['sections'][0]['hits'][2]['result']['full_title'])
		# itembtn4 = bot.send_message(message.chat.id, res.json()['response']['sections'][0]['hits'][3]['result']['full_title'])
		# itembtn5 = bot.send_message(message.chat.id, res.json()['response']['sections'][0]['hits'][4]['result']['full_title'])
	markup = types.InlineKeyboardMarkup(row_width=3)
	itembtn1 = types.InlineKeyboardButton(res.json()['response']['sections'][0]['hits'][0]['result']['full_title'], callback_data = res.json()['response']['sections'][0]['hits'][0]['result']['url'])
	itembtn2 = types.InlineKeyboardButton(res.json()['response']['sections'][0]['hits'][1]['result']['full_title'], callback_data = res.json()['response']['sections'][0]['hits'][1]['result']['url'])
	itembtn3 = types.InlineKeyboardButton(res.json()['response']['sections'][0]['hits'][2]['result']['full_title'], callback_data = res.json()['response']['sections'][0]['hits'][2]['result']['url'])
	markup.add(itembtn1)
	markup.add(itembtn2)
	markup.add(itembtn3)
	bot.send_message(message.chat.id, "Choose a song:", reply_markup = markup)

	# except: 
		# pass
	# bot.send_message(message.chat.id, "you`ve chosen 'v'")
	
@bot.callback_query_handler(func = lambda call: call.data )
def get_day(call):
	print(call.data)
	data = requests.get(call.data)
	html = bs4.BeautifulSoup(data.text, "html.parser")
	count = html.select('.lyrics p')
	print(len(count))


	lines = count[0].contents
	print(lines)
	lyrics = ""
	for i in lines:
		# print(i.contents)
		if ">" in str(i) or "<" in str(i) or str(i) == "" or str(i) == "\n":
			continue
		lyrics += str(i)[1:] + "\n"

	bot.send_message(call.message.chat.id, lyrics)
# def get_song_links(url):o
#    html = urlopen(url).read()
#     print html 
#    soup = BeautifulSoup(html, "lxml")
#    container = soup.find("div", "container")
#     song_links = [BASE_URL + dd.a["href"] for dd in container.findAll("dd")]

#     print song_links

# get_song_links(artist_url)
# for link in soup.find_all('a'):
#    print(link.get('href'))




# from apiclient.discovery import build
# from apiclient.errors import HttpError
# from oauth2client.tools import argparser


# # Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# # tab of
# #   https://cloud.google.com/console
# # Please ensure that you have enabled the YouTube Data API for your project.
# DEVELOPER_KEY = 'AIzaSyB4uXZz9hNHK7sjAXr5nhw3a4hmfQSvpL8'
# YOUTUBE_API_SERVICE_NAME = "youtube"
# YOUTUBE_API_VERSION = "v3"

# def youtube_search(options):
#   youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
#     developerKey=DEVELOPER_KEY)

#   # Call the search.list method to retrieve results matching the specified
#   # query term.
#   search_response = youtube.search().list(
#     q=options.q,
#     part="id,snippet",
#     maxResults=options.max_results
#   ).execute()

#   videos = []
#   channels = []
#   playlists = []

#   # Add each result to the appropriate list, and then display the lists of
#   # matching videos, channels, and playlists.
#   for search_result in search_response.get("items", []):
#     if search_result["id"]["kind"] == "youtube#video":
#       videos.append("%s (%s)" % (search_result["snippet"]["title"],
#                                  search_result["id"]["videoId"]))
#     elif search_result["id"]["kind"] == "youtube#channel":
#       channels.append("%s (%s)" % (search_result["snippet"]["title"],
#                                    search_result["id"]["channelId"]))
#     elif search_result["id"]["kind"] == "youtube#playlist":
#       playlists.append("%s (%s)" % (search_result["snippet"]["title"],
#                                     search_result["id"]["playlistId"]))

#   print "Videos:\n", "\n".join(videos), "\n"
#   print "Channels:\n", "\n".join(channels), "\n"
#   print "Playlists:\n", "\n".join(playlists), "\n"


# if __name__ == "__main__":
#   argparser.add_argument("--q", help="Search term", default="Google")
#   argparser.add_argument("--max-results", help="Max results", default=25)
#   args = argparser.parse_args()

#   try:
#     youtube_search(args)
#   except HttpError, e:
#     print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)


bot.polling()








