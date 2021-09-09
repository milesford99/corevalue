from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://values.venzagroup.com")
js = "function updateCoreValue(user_id,core_value,oof){if(oof===undefined){oof=0}updating=true;var token;$.ajax({method:'GET',url:'/token',dataType:'json'}).done(function(response){token=response.token});$.ajax({type:'POST',url:'index.php/selection/'+user_id,dataType:'json',data:{_method:'PUT',core_value:core_value,oof:oof},headers:{'X-CSRF-TOKEN':token}}).done(function(response){updating=false;if(core_value===0&&$('#user_id-'+user_id).parent().attr('id')!='gallery'){moveTo($('#user_id-'+user_id),'#gallery')}else if($('#user_id-'+user_id).parent().attr('id')!='value'+core_value){moveTo($('#user_id-'+user_id),'#value'+core_value)}if(oof===1){$('#user_id-'+user_id).addClass('oof')}else{$('#user_id-'+user_id).removeClass('oof')}}).fail(function(response){updating=false}).always(function(){$('#user_id-'+user_id).removeAttr('data-x').removeAttr('data-y').removeAttr('style')})}updateCoreValue(59,2,0);updateCoreValue(60,1,0);updateCoreValue(61,3,0);updateCoreValue(62,5,0);updateCoreValue(63,3,0);updateCoreValue(65,3,0);updateCoreValue(66,2,0);updateCoreValue(67,2,0);updateCoreValue(68,1,0);updateCoreValue(69,3,0);updateCoreValue(70,1,0);updateCoreValue(79,2,0);"

driver.execute_script(js)