import requests
import userdata
import json
class Cunzheng():
	def __init__(self):
		pass
	def token(self,ip,url_token,username,password,grant_type):
		hosttoken = ip + url_token
		# print(hostadd)
		heards1 = {"Authorization": "Basic YW1zOmFtcw=="}
		data = {"username": username, "password": password, "grant_type": grant_type}
		# print('data的类型',type(data))
		r = requests.post(hosttoken, data=data, headers=heards1)
		try:
			a = r.json()
			au = a["access_token"]
			#print(a)
			#print(type(a))
			return au
		except:
			print(r.text)
	def uploadFileBatch(self,ip,url_uploadFileBatch,au,cert,file_path):
		hostuploadFileBatch=ip + url_uploadFileBatch
		Authorization = 'Bearer ' + au
		heards2 = {"Authorization": Authorization}
		#files1= {'file':open(file_path,'rb')}
		files1 = {"file": open(file_path, 'rb'), "Content-Type": "application/octet-stream",
				"Content-Disposition": "form-data"}
		form_data = {"cert":cert}
		r_upload = requests.post(hostuploadFileBatch, files=files1, data=form_data, headers=heards2)
		b = r_upload.json()
		if b['code'] == '0000':
			return b['data'][0]
		else:print(b)

		# try:
		# 	b = r_upload.json()
		# 	print(b)
		# except:
		# 	b = r_upload.json()
		# 	print(r_upload)
		# return b['data'][0]

	def saveEvidence(self,ip,url_saveEvidence,au,username,cert,privatekey,pin_code,file_info):
		if isinstance(file_info,dict):
			hostsaveEvidence = ip + url_saveEvidence
			Authorization = 'Bearer ' + au
			heards2 = {"Authorization": Authorization}
			datasaveEvidence = {
			"user_name": username,
			"cert": cert,
			"private_key": privatekey,
			"pin_code": pin_code,
			"saveEvidenceInfo": {
				"file_id": file_info["file_id"],
				"ipfs_hash": file_info["ipfs_hash"],
				"file_hash": file_info["file_hash"],
				"file_name": file_info["file_name"],
				"file_type": file_info["file_type"],
				"file_pwd": file_info["file_pwd"]
			}
		}
			try:
				c = requests.post(hostsaveEvidence, json=datasaveEvidence, headers=heards2)
				d=c.json()
		# print(c.text)
		# print(type(c))
			except:
				print(c.text)
			return d
		else:
			print('file_info无实际数据')
	def saveEvidence_hash(self,ip,url_saveEvidence,au,username,cert,privatekey,pin_code,file_hash,file_name):
		hostsaveEvidence = ip + url_saveEvidence
		Authorization = 'Bearer ' + au
		heards2 = {"Authorization": Authorization}
		datasaveEvidence = {
			"user_name": username,
			"cert": cert,
			"private_key": privatekey,
			"pin_code": pin_code,
			"saveEvidenceInfo": {
				"file_id": '',
				"ipfs_hash": '',
				"file_hash": file_hash,
				"file_name": file_name,
				"file_type": '05',
				"file_pwd": ''
			}
		}
		try:
			c = requests.post(hostsaveEvidence, json=datasaveEvidence, headers=heards2)
			d=c.json()
		# print(c.text)
		# print(type(c))
		except:
			print(c.text)
		return d
	def endorseProposal(self,ip,url_endorseProposal,au,saveEvidence_data):
		'''
		证据信息上链第二步
		'''
		if isinstance(saveEvidence_data, dict):
			hostendorseProposal = ip + url_endorseProposal
			Authorization = 'Bearer ' + au
			heards2 = {"Authorization": Authorization}
			data4 = {"result": saveEvidence_data["data"]}
			d = requests.post(hostendorseProposal, json=data4, headers=heards2)
			# print(d.text)
			try:
				d1 = d.json()
		# print(d1["data"]["endorse_response"])
			except:
				print(d.text)
			return d1
		else:
			print('saveEvidence_data无数据')
	def evidenceChain(self,ip,url_evidenceChain,au,username,cert,privatekey,pin_code,endorseProposal_data):
		'''
		证据信息上链第三步
		'''
		if isinstance(endorseProposal_data, dict):
			hostevidenceChain = ip + url_evidenceChain
			Authorization = 'Bearer ' + au
			heards2 = {"Authorization": Authorization}
			data5 = {
			"user_name": username,
			"cert": cert,
			"private_key": privatekey,
			"pin_code": pin_code,
			"chainVo": {
				"endorse_response": endorseProposal_data["data"]["endorse_response"]
			}
		}
		# except:
		# 	print('赋值有误')
		# print(data5)
			try:
				e = requests.post(hostevidenceChain, json=data5, headers=heards2)
			# print(e.text)
				e1 = e.json()
			except:
				print(e.text)
			return e1
		else:
			print('endorseProposal_data无数据')
	def uploadNotaryChain(self,ip,au,url_uploadNotaryChain,evidenceChain_data):
		'''
		证据信息上链第四步
		'''
		if isinstance(evidenceChain_data, dict):
			Authorization = 'Bearer ' + au
			heards2 = {"Authorization": Authorization}
			hostuploadNotaryChain = ip + url_uploadNotaryChain
			data6 = {
			"block_event_listener_request": evidenceChain_data['data']['block_event_listener_request'],
			"sign_transaction_request": evidenceChain_data['data']['sign_transaction_request'],
			"transaction_event_listener_request": evidenceChain_data['data']['transaction_event_listener_request'],
			"txid": "e1['data']['txid']"
		}
			try:
				f = requests.post(hostuploadNotaryChain, json=data6, headers=heards2)
				f1 = f.json()
				if f1['success'] == True:
					print('证据存证成功')
				else:
					print('证据存证失败')
			except:
				a=print(f.text)
			return f1
		else:
			print('evidenceChain_data无数据')
if __name__ == '__main__':
	'''
	哈希存证时，请输入或者修改file_hash和file_name
	'''
	file_hash='1025a6d6ca00658bfff9097dda8b8201'
	file_name='哈希存证测试12'
	cz=Cunzheng()
	url_token=userdata.url_token
	url_uploadFileBatch=userdata.url_uploadFileBatch
	url_saveEvidence=userdata.url_saveEvidence
	url_endorseProposal=userdata.url_endorseProposal
	url_evidenceChain=userdata.url_evidenceChain
	url_uploadNotaryChain=userdata.url_uploadNotaryChain
	cert=userdata.cert
	privatekey=userdata.privatekey
	pin_code=userdata.pin_code
	ip=userdata.ip
	file_path=userdata.file_path
	username=userdata.username
	password=userdata.password
	grant_type=userdata.grant_type
	#获取用户token
	au=cz.token(ip,url_token,username,password,grant_type)
	#print(au)
	#存证文件上传
	#file_info=cz.uploadFileBatch(ip,url_uploadFileBatch,au,cert,file_path)l
	#print(file_info)
	#引用存证哈希信息
	b=cz.saveEvidence_hash(ip,url_saveEvidence,au,username,cert,privatekey,pin_code,file_hash,file_name)
	#print(b)
	#引用证据信息上链（第二步）
	endorseProposal_data=cz.endorseProposal(ip,url_endorseProposal,au,b)
	#print(endorseProposal_data)
	#引用证据信息上链（第三步）
	d=cz.evidenceChain(ip,url_evidenceChain,au,username,cert,privatekey,pin_code,endorseProposal_data)
	# print(d)
	# print(type(d))
	#引用证据信息上链（第四步）
	f=cz.uploadNotaryChain(ip,au,url_uploadNotaryChain,evidenceChain_data=d)
	#print(f)
