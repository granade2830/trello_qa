def script_check():
	address = 'https://trello.com/'

		
	testing_pattern = 0
	while testing_pattern < 2: # check both Chrome 
		if testing_pattern == 0:
			browser = webdriver.Firefox()
		elif testing_pattern == 1:
			browser = webdriver.Chrome()
		browser.get(address)
		ajax_complete(browser)
		doc = lxml.html.fromstring(browser.page_source)
		if testing_pattern == 0:
			driver = 'Firefox'
		elif testing_pattern ==1:
			driver = 'Chrome'
		testing_pattern += 1


		if not doc.xpath('//h1[@style="margin: 0 auto; max-width: 900px;"]/text()') == ['Trello is the free, flexible, and visual way to organize anything with anyone.']:
			print "Trello Intro 1 wrong", driver
		if not doc.xpath('//a[@class="quiet"]/@href') == ['/login']:
			print "login 1 wrong", driver
		if not doc.xpath('//div[@class="section-wrapper text-center"]/img/@src') == ['https://d2k1ftgv7pobq7.cloudfront.net/meta/p/res/images/c13d1cd96a2cff30f0460a5e1860c5ea/header-logo-blue.svg']:
			print "logo wrong", driver
		if not doc.xpath('//div[@class="layout-twothirds-center text-center"]/p/text()') == [' \n            Drop the lengthy email threads, out-of-date spreadsheets,\n            no-longer-so-sticky notes, and clunky software for managing\n            your projects. Trello lets you see everything about your\n            project in a single glance.\n ', ' ',' ',' \n            Trello is simple on the surface, but cards have ','. Post comments for instant\n            feedback. Upload files from your computer, Google Drive, Dropbox,\n            Box, and OneDrive. Add checklists, labels, due dates, and more.\n            Notifications make sure you always know when important stuff\n            happens.\n ',' \n            ',' for managing your projects, and become one of\n            the millions of people to fall in love with Trello. You can add\n            as many boards and people as you want with your free account.\n ']:
			print "layout-twothirds-center text-center wrong", driver
		if not doc.xpath('//div[@class="layout-twothirds-center"]/p/text()') == [u' \n            This is a Trello board. It\u2019s a list of lists filled with cards, used\n            with a team or by yourself.\n ',' \n            Drag and drop cards between lists to show progress.\n            Add as many people as you need and drag them to cards.\n            Add and reorder lists as you need. ','\n ',u' \n            You\u2019ll see everything about your project just by glancing at the\n            board, and it all updates in real-time. There\u2019s nothing to set up\n            and everyone gets it instantly.\n ']:
			print "layout-twothirds-center wrong", driver
		if not doc.xpath('//div[@class="layout-twothirds-center text-center"]/p/strong/text()') == ['everything\n            you need to get stuff done','Ditch the sticky notes, spreadsheets, email, and clunky\n            software']:
			print "layout-twothirds-center_strong wrong", driver
		if not doc.xpath('//div[@class="layout-twothirds-left"]/p/text()') == [' \n            Trello stays perfectly in sync across all your devices,\n            wherever you are. There are fast and intuitive apps for\n            the web, Android phones and tablets, iPhone and iPad and Kindle Fire.\n ',' ',' ',' ',' ', u' \n            Trello will never overwhelm you with features you won\u2019t use.\n            For those who want more out of their boards, there are\n            ',u' like calendar, card aging, and voting,\n            that you can turn on. It\u2019s a way to offer more without\n            cluttering things for everyone.\n ']:
			print "layout-twothirds-left", driver
		if not doc.xpath('//div[@class="layout-twothirds-left"]/p/strong/text()') == ['Power-Ups']:
			print "layout-twothirds-left strong", driver
		if not doc.xpath('//div[@class="text-center section-love-header"]/p/text()') == [' \n            ',' and companies of all kinds and\n            sizes love using Trello.\n ']:
			print "text-center section-love-header", driver
		if not doc.xpath('//div[@class="text-center section-love-header"]/p/strong/text()') == ['Millions of people']:
			print "text-center section-love-header strong", driver
		if not len(doc.xpath('//div[@class="text-center layout-company-logos"]/img')) == 9 :
			print "company number", driver
		if not len(doc.xpath('//div[@class="layout-callout-left layout-callout-down2"]/img')) == 1:
			print "Trello logo", driver
		if not doc.xpath('//div[@class="layout-twothirds-right"]/p/text()') == [' \n            Does your company or organization need extra administrative\n            control and team super powers? We made ',' for you.\n ',' ',' ']:
			print "layout-twothirds-right", driver
		if not doc.xpath('//div[@class="layout-twothirds-right"]/p/strong/text()') == ['Business\n            Class']:
			print "layout-twothirds-right strong", driver
		if not doc.xpath('//div[@class="layout-twothirds-right"]/p[2]/a/text()') == ['Learn more about Business Class']:
			print "layout-twothirds-right wrong", driver
		if not doc.xpath('//div[@class="layout-twothirds-center text-center"]/p/strong/text()') == ['everything\n            you need to get stuff done', 'Ditch the sticky notes, spreadsheets, email, and clunky\n            software']:
			print "layout-twothirds-center text-center wrong", driver
		if not doc.xpath('//a[@class="button button-green"]/text()') == [u' Sign Up \u2013 It\u2019s Free. ', u' Sign Up \u2013 It\u2019s Free. ']:
			print "button button-green", driver
		if not len(doc.xpath('//div[@class="layout-callout-left layout-callout-up1"]/img')) == 1:
			print "husky logo", driver
		if not doc.xpath('//div[@class="layout-twothirds-right layout-callout-up1"]/p/text()') == [' Oh, and this is ', u' You\u2019ll see him around. ']:
			print "layout-twothirds-right layout-callout-up1", driver
		if not doc.xpath('//div[@class="layout-twothirds-right layout-callout-up1"]/p/strong/text()') == ['Taco, our spokes-husky.']:
			print 'layout-twothirds-right layout-callout-up1 strong', driver
		if not doc.xpath('//footer[@class="quiet"]/ul/li/a/text()') == ['Tour','Pricing','Apps', 'Jobs','Blog', 'Developers','About','Help','Legal']:
			print "footer", driver
		if not doc.xpath('//footer[@class="quiet"]/p/text()') == [u' \xa9 Copyright 2016, Trello, Inc. All rights reserved. ']:
			print "copyright", driver