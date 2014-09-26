# -*- coding: utf-8 -*-
from flask import render_template, request, make_response, flash, url_for, redirect , jsonify

from apps.models import	Article,Comment
from sqlalchemy import desc
from apps import app, db





#
# division make page
#
@app.route('/make_division', methods=['GET','POST'])
def make_division():

	if request.method == 'GET':
		return render_template("divide/make_division.html", active_tab='make_division')
	elif request.method == 'POST':
		division_row = request.form['row']
		division_col = request.form['col']

		resp = make_response(redirect(url_for('article_list')))
		resp.set_cookie('division_row',division_row)
		resp.set_cookie('division_col',division_col)
		for i in range(int(division_row)*int(division_col)):
			block_url = "block_url"+str(i)
			resp.set_cookie(block_url,"")
			block_url_img = "block_url_img"+str(i)
			resp.set_cookie(block_url_img,"")
			block_widget = "block_widget"+str(i)
			resp.set_cookie(block_widget,"")

		flash(u'화면분할이 완료되었습니다.','success')
		return resp


@app.route('/unset_division', methods=['GET'])
def unset_division():
	block_num = request.args.get('block_num',0,type = int)
	block_url = "block_url"+str(block_num)
	block_widget = "block_widget"+str(block_num)
	
	"""resp = make_response(redirect(url_for('article_list')))
	resp.set_cookie(block_url,"")
	resp.set_cookie(block_widget,"")"""

	return jsonify(block_num = block_num)

#
# delete_cookie page
#

@app.route('/delete_cookie', methods=['GET'])
def delete_cookie():
	resp = make_response(redirect(url_for('article_list')))
	division_row = request.cookies.get('division_row')
	division_col = request.cookies.get('division_col')
	for i in range(int(division_row)*int(division_col)):
			block_url = "block_url"+str(i)
			resp.set_cookie(block_url,"")
			block_widget = "block_widget"+str(i)
			resp.set_cookie(block_widget,"")
	resp.set_cookie('division_row',"0")
	resp.set_cookie('division_col',"0")
	
	return resp



@app.route('/set_block<int:block_num>', methods=['GET','POST'])
def set_block(block_num):
	if request.method == 'GET':
		return render_template("divide/set_indivisual.html",block_num = block_num)
	elif request.method == 'POST':
		url = request.form['url']
		widget = request.form['widget']
		block_number = request.form['block_num']

		resp = make_response(redirect(url_for('article_list')))
		if url:
			block_url = "block_url"+str(block_number)
			resp.set_cookie(block_url,url)
			flash(u'url 등록이 완료되었습니다.','success')
		elif widget:
			block_widget = "block_widget"+str(block_number)
			resp.set_cookie(block_widget,widget)
			flash(u'widget 등록이 완료되었습니다.','success')
			
		return resp

@app.route('/set_naverblock<int:block_num>', methods=['GET','POST'])
def set_naverblock(block_num):
	resp = make_response(redirect(url_for('article_list')))
	block_url = "block_url"+str(block_num)
	block_url_img = "block_url_img" + str(block_num)
	resp.set_cookie(block_url,"http://www.naver.com")
	resp.set_cookie(block_url_img,"./static/images/naver.PNG")
	flash(u'네이버 등록이 완료되었습니다.','success')

	return resp

@app.route('/set_googleblock<int:block_num>', methods=['GET','POST'])
def set_googleblock(block_num):
	resp = make_response(redirect(url_for('article_list')))
	block_url = "block_url"+str(block_num)
	block_url_img = "block_url_img" + str(block_num)
	resp.set_cookie(block_url,"http://www.google.com")
	resp.set_cookie(block_url_img,"./static/images/google.PNG")
	flash(u'구글 등록이 완료되었습니다.','success')

	return resp

@app.route('/set_facebookblock<int:block_num>', methods=['GET','POST'])
def set_facebookblock(block_num):
	resp = make_response(redirect(url_for('article_list')))
	block_url = "block_url"+str(block_num)
	block_url_img = "block_url_img" + str(block_num)
	resp.set_cookie(block_url,"http://www.facebook.com")
	resp.set_cookie(block_url_img,"./static/images/facebook.PNG")
	flash(u'facebook 등록이 완료되었습니다.','success')

	return resp

@app.route('/set_daumblock<int:block_num>', methods=['GET','POST'])
def set_daumblock(block_num):
	resp = make_response(redirect(url_for('article_list')))
	block_url = "block_url"+str(block_num)
	block_url_img = "block_url_img" + str(block_num)
	resp.set_cookie(block_url,"http://www.daum.net")
	resp.set_cookie(block_url_img,"./static/images/daum.PNG")
	flash(u'다음 등록이 완료되었습니다.','success')

	return resp

@app.route('/set_youtubeblock<int:block_num>', methods=['GET','POST'])
def set_youtubeblock(block_num):
	resp = make_response(redirect(url_for('article_list')))
	block_url = "block_url"+str(block_num)
	block_url_img = "block_url_img" + str(block_num)
	resp.set_cookie(block_url,"http://www.youtube.com")
	resp.set_cookie(block_url_img,"./static/images/youtube.jpg")
	flash(u'YouTube 등록이 완료되었습니다.','success')

	return resp

@app.route('/set_twitterblock<int:block_num>', methods=['GET','POST'])
def set_twitterblock(block_num):
	resp = make_response(redirect(url_for('article_list')))
	block_url = "block_url"+str(block_num)
	block_url_img = "block_url_img" + str(block_num)
	resp.set_cookie(block_url,"https://twitter.com")
	resp.set_cookie(block_url_img,"./static/images/twitter.jpg")
	flash(u'트위터 등록이 완료되었습니다.','success')

	return resp

@app.route('/set_instagramblock<int:block_num>', methods=['GET','POST'])
def set_instagramblock(block_num):
	resp = make_response(redirect(url_for('article_list')))
	block_url = "block_url"+str(block_num)
	block_url_img = "block_url_img" + str(block_num)
	resp.set_cookie(block_url,"http://korstagram.com")
	resp.set_cookie(block_url_img,"./static/images/instagram.png")
	flash(u'인스타그램 등록이 완료되었습니다.','success')

	return resp

@app.route('/unset_block<int:block_num>', methods=['GET','POST'])
def unset_block(block_num):
	resp = make_response(redirect(url_for('article_list')))
	
	block_url = "block_url"+str(block_num)
	resp.set_cookie(block_url,"")
	flash(u'url 해제가 완료되었습니다.','success')

	return resp