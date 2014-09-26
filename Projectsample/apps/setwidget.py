# -*- coding: utf-8 -*-
from flask import render_template, request, make_response, flash, url_for, redirect , jsonify

from apps.models import	Article,Comment
from sqlalchemy import desc
from apps import app, db

#
# division make page
#
@app.route('/make_widget', methods=['GET'])
def make_widget():
	return render_template("widget/setwidget.html", active_tab='setwidget')


@app.route('/set_naversearch', methods=['GET','POST'])
def set_naversearch():
	resp = make_response(redirect(url_for('article_list')))
	resp.set_cookie('search',"naver")
	flash(u'네이버 위젯 등록이 완료되었습니다.','success')
	return resp

@app.route('/set_googlesearch', methods=['GET','POST'])
def set_googlesearch():
	resp = make_response(redirect(url_for('article_list')))
	resp.set_cookie('search',"google")
	flash(u'구글 위젯 등록이 완료되었습니다.','success')
	return resp
	