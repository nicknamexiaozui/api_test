from cunzheng import Cunzheng
import userdata
if __name__ == '__main__':
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
	print('获取到的token:%s'%au)
	#存证文件上传
	file_info=cz.uploadFileBatch(ip,url_uploadFileBatch,au,cert,file_path)
	print('文件上传的信息:%s'%file_info)
	#引用存证证据信息
	b=cz.saveEvidence(ip,url_saveEvidence,au,username,cert,privatekey,pin_code,file_info)
	print(b)
	#引用证据信息上链（第二步）
	endorseProposal_data=cz.endorseProposal(ip,url_endorseProposal,au,b)
	print(endorseProposal_data)
	#引用证据信息上链（第三步）
	d=cz.evidenceChain(ip,url_evidenceChain,au,username,cert,privatekey,pin_code,endorseProposal_data)
	#print(d)
	# print(type(d))
	#引用证据信息上链（第四步）
	f=cz.uploadNotaryChain(ip,au,url_uploadNotaryChain,evidenceChain_data=d)
	print(f)
