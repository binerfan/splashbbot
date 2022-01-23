API_KEY = '5073218880:AAGJbS0sw6ynmbJXbTZvxotAZtx76X-ygdI'
import telebot
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])

def start(message):
  bot.send_message(message.chat.id, "سلام! به ربات اسپلش خوش آمدید. برای اطلاع از غایبان هر تیم، با زدن اسلش(/) و بعد نام تیم مورد نظر از غایبان آن تیم با خبر شوید. مثلا /BostonCeltics \n اگر از آیدی تیم مورد نظر خود مطمئن نیستید،  با فرستادن /teamlist برای من لیست کامل آیدی تیم ها را دریافت کنید! \n اگر به دنبال لينک هاي پخش ززنده هستيد، /linklist را براي من ارسال کنيد\n اگر دچار مشکل شدید، /help. \n برای اطلاعات بیشتر، /about." )

@bot.message_handler(commands=['teamlist'])
def teamlist(message):
  bot.send_message(message.chat.id, "1./AtlantaHawks \n2./BostonCeltics \n3./BrooklynNets \n4./CharlotteHornets \n5./ChicagoBulls \n6./ClevelandCavaliers \n7./DallasMavericks \n8./DenverNuggets \n9./DetroitPistons \n10./GoldenStateWarriors \n11./HoustonRockets \n12./IndianaPacers \n13./LosAngelesClippers \n14./LosAngelesLakers \n15./MemphisGrizzlies \n16./MiamiHeat \n17./MilwaukeeBucks \n18./MinnesotaTimberwolves \n19./NewOrleansPelicans \n20./NewYorkKnicks \n21./OklahomaCityThunder \n22./OrlandoMagic \n23./Philadelphia76ers \n24./PhoenixSuns \n25./PortlandTrailBlazers \n26./SacramentoKings \n27./SanAntonioSpurs \n28./TorontoRaptors \n29./UtahJazz \n30./WashingtonWizards" )

@bot.message_handler(commands=['linklist'])
def linklist(message):
  bot.send_message(message.chat.id, "1. https://www.strikeout.cc/basketball \n2. http://nbastream.io \n3. http://nbastream.nu \n4. http://freestreams-live1.com \n5. http://live.harleyquinnwidget.live \n6. https://sportshub.stream/basketball-live-streams \n7. https://sports24.stream/nba \n8. https://daddylive.live \n9. https://www.vipboxtv.se/basketball-stream ")

@bot.message_handler(commands=['about'])
def about(message):
  bot.reply_to(message, "این ربات برای اطلاع بهتر شما عزیزان از غایبین هر تیم طراحی شده است. \nتمامی حقوق این ربات به رسانه اسپلش باز میگردد. \nآیدی کانال اسپلش: @SplashBBall ")

@bot.message_handler(commands=['AtlantaHawks'])
def hawks(message):
  bot.reply_to(message, "OUT: \n1. Bogdan Bogdanovic \n2. Sharife Cooper \n3. Jalen Johnson \n \n QUESTIONABLE: \n1. Danilo Gallinari \n2. kevin Huerter  ") 
@bot.message_handler(commands=['BostonCeltics'])
def celtics(message):
  bot.reply_to(message, "OUT: \n1. Bruno Fernando \n2. PJ Dozier \n3. Bol Bol \n4. Brodric Thomas \n5. Sam Hauser")

@bot.message_handler(commands=['BrooklynNets'])
def nets(message):
  bot.reply_to(message, "OUT: \n1. Joe Harris  \n2. David Duke.jr \n3. Kevin Durant \n4. Paul Millsap \n \n QUESTIONABLE: \n1. Nic claxton")

@bot.message_handler(commands=['CharlotteHornets'])
def hornets(message):
  bot.reply_to(message, "OUT: \n1. Jaden McDaniels ")

@bot.message_handler(commands=['ChicagoBulls'])
def bulls(message):
  bot.reply_to(message, "OUT: \n1. Patrick Williams  \n2. Javonte Green \n3. Derrick Jones.jr \n4. Zach LaVine \n5. Zo Ball \n6. Alex Caruso")

@bot.message_handler(commands=['ClevelandCavaliers'])
def cavs(message):
  bot.reply_to(message, "OUT: \n1. Rajon Rondo \n2. Collin Sexton  \n3. Ricky Rubio \n4. Lamar Stevens ")

@bot.message_handler(commands=['DallasMavericks'])
def mavs(message):
  bot.reply_to(message, "OUT: \n1. Sterling Brown")

@bot.message_handler(commands=['DenverNuggets'])
def denver(message):
  bot.reply_to(message, "OUT: \n1. Jamal Murray  \n2. Michael Porter.jr  \n3. Vlatko Cancar \n4. JaMychal Green ")
 
@bot.message_handler(commands=['DetroitPistons'])
def pistons(message):
  bot.reply_to(message, "OUT: \n1. Rodney McGruder (SG) \n2. Cade Cunningham (PG) \n3. Saben Lee (PG) \n4. Killian Hayes (PG) \n5. Kelly Olynyk (C) \n6. Jerami Grant (PF) \n7. Isaiah Stewart (C) \n8. Chris Smith (SF)")

@bot.message_handler(commands=['GoldenStateWarriors'])
def golden(message):
  bot.reply_to(message, "OUT: \n1. James Wiseman \n2. Draymond Green \n3. Andre Igoudala ")

@bot.message_handler(commands=['HoustonRockets'])
def houston(message):
  bot.reply_to(message, "OUT: \n1. John Wall  ")

@bot.message_handler(commands=['IndianaPacers'])
def pacers(message):
  bot.reply_to(message, "OUT: \n1. TJ McConnell  \n2. TJ Warren \n3. Myles Turner \n4. Domantas Sabonis \n \n QUESTIONABLE: \n1.Caris LeVert \n2. Malcolm Brogdon ")

@bot.message_handler(commands=['LosAngelesClippers'])
def clipp(message):
  bot.reply_to(message, "OUT: \n1. Paul George \n2. Jason Preston \n3. Kawhi Leonard \n4. Keon Johnson")

@bot.message_handler(commands=['LosAngelesLakers'])
def lakers(message):
  bot.reply_to(message, "OUT: \n1. Kendrick Nunn \n2. Mason jones \n3. Sekou Doumboya \n \n QUESTIONABLE: \n1. Anthony Davis")

@bot.message_handler(commands=['MemphisGrizzlies'])
def memphis(message):
  bot.reply_to(message, "OUT:  \n1. Yves Pons \n2. Dillon Brooks \n3. Killian Tillie \n4. Desmond Bane \n5. Kyle Anderson \n \n QUESTIONABLE: \n1. Steve Adams \n2. Brandon Clarke")

@bot.message_handler(commands=['MiamiHeat'])
def heat(message):
  bot.reply_to(message, "OUT: \n1. Victor Oladipo  \n2. Markieff Morris  \n3. KZ Okpala \n4. Kyle Lowry \n5. Tyler Herro \n \n QUESTIONABLE: \n1. PJ Tucker")

@bot.message_handler(commands=['MilwaukeeBucks'])
def bucks(message):
  bot.reply_to(message, "OUT:\n1. Brook Lopez  ")

@bot.message_handler(commands=['MinnesotaTimberwolves'])
def wolves(message):
  bot.reply_to(message, "OUT: \n1. Jordan McLaughlin \n \n QUESTIONABLE: \n1. Pat Bev")

@bot.message_handler(commands=['NewOrleansPelicans'])
def pelicans(message):
  bot.reply_to(message, "OUT: \n1. Kira Lewis.jr  \n2. Zion Williamson \n \n QUESTIONABLE: \n1. Brandon Ingram  ")

@bot.message_handler(commands=['NewYorkKnicks'])
def knicks(message):
  bot.reply_to(message, "OUT:\n1. Derrick ( GOAT ) Rose  \n2. Cam Reddish \n3. Nerlens Noel \n4. Ryan Arcidiacano  \n \n QUESTIONABLE: \n1. Luka Samanic ")

@bot.message_handler(commands=['OklahomaCityThunder'])
def okc(message):
  bot.reply_to(message, "OUT: \n1. Vit Krejci  ")

@bot.message_handler(commands=['OrlandoMagic'])
def magic(message):
  bot.reply_to(message, "OUT: \n1. Terrence Ross (SG) \n2. RJ Hampton (PG) \n3. Jalen Suggs (SG) \n4. Markelle Fultz (PG) \n5. Moritz Wagner (C) \n6. Jonathan Isaac (PF) \n7. Michael Carter-Williams (PG) \n8. Ignas Brazdeikis (SF)\n9. Mo Bamba (C) \n10. Mychal Mulder (G) \n11. E'twaun Moore (G)")

@bot.message_handler(commands=['Philadelphia76ers'])
def ers(message):
  bot.reply_to(message, "OUT: \n1.  Ben Simmons  \n2. Shake Milton  \n3. Danny Green \n4. Matisse Thybulle \n5. Seth Curry ")

@bot.message_handler(commands=['PhoenixSuns'])
def suns(message):
  bot.reply_to(message, "OUT: \n1. Abdel Nader (SF) \n2. Dario Saric  \n3. Frank Kaminsky (C) \n4. D Ayton ")

@bot.message_handler(commands=['PortlandTrailBlazers'])
def blazers(message):
  bot.reply_to(message, "OUT: \n1. Larry Nance.jr \n2. Damian Lillard \n3. Norman Powell \n4. Cody Zeller  " )

@bot.message_handler(commands=['SacramentoKings'])
def kings(message):
  bot.reply_to(message, "OUT:  \n1. Tyrese Haliburton ")

@bot.message_handler(commands=['SanAntonioSpurs'])
def spurs(message):
  bot.reply_to(message, "OUT: \n1. Josh Primo \n2. Zach Collins \n3. Devontae Cacock")

@bot.message_handler(commands=['TorontoRaptors'])
def raptors(message):
  bot.reply_to(message, "OUT: \n1. Goran dragic \n2. Khem Birch \n3. Gary Trent.jr ")

@bot.message_handler(commands=['UtahJazz'])
def jazz(message):
  bot.reply_to(message, "OUT: \n1. D Mitchell \n \n QUESTIONABLE: \n1. Rudy Gobert \n2. Hassan Whiteside  ")

@bot.message_handler(commands=['WashingtonWizards'])
def wizards(message):
  bot.reply_to(message, "QUESTOINABLE: \n1. Kyle Kuzma ")

@bot.message_handler(commands=['help'])
def help(message):
  bot.reply_to(message, "غایبان تیم ها از دو بخش تشکیل شده اند. بخش اول کسانی که قطعا به بازی تیم هایشان نمیرسند (out) . و بخش دوم کسانیکه هنوز وضعیتشان مشخص نیست (questionable) \n اگر سوال دیگری داشتید، حتما در گروه اسپلش مطرح کنید! \n  @SplashBBallGP")

bot.polling() 
