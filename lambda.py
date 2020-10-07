class TimerIntentHandler(AbstractRequestHandler):
    #only can be called if there if timer hasn't been paused
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("TimerIntent")(handler_input)
    def handle(self, handler_input):

        permissions = handler_input.request_envelope.context.system.user.permissions
        if not (permissions and permissions.consent_token):
            return (
                handler_input.response_builder
                .speak("Please give permissions to set timers using the alexa app.")
                .set_card(
                    AskForPermissionsConsentCard(permissions=REQUIRED_PERMISSIONS)
                )
                .response
            )
        timer_service = handler_input.service_client_factory.get_timer_management_service()                        
        timer_response = timer_service.create_timer(timer_request)
        if str(timer_response.status) == "Status.ON":
            session_attr = handler_input.attributes_manager.session_attributes
            if not session_attr:
                session_attr['lastTimerId'] = timer_response.id
                return handler_input.response_builder.speak("Subscibed user timer started").response
        else:
            # logging.info("Something went wrong, subscribed!")
            return handler_input.response_builder.speak("Something went wrong, subscribed").response
            
'''
#ERROR:
[ERROR]	2020-10-07T00:42:38.223Z	50f7b68d-55d1-4bbd-a25b-e3fd8f32a238	Couldn't parse response body: <!doctype html><html lang="en"><head><title>HTTP Status 500 – Internal Server Error</title><style type="text/css">H1 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:22px;} H2 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:16px;} H3 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:14px;} BODY {font-family:Tahoma,Arial,sans-serif;color:black;background-color:white;} B {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;} P {font-family:Tahoma,Arial,sans-serif;background:white;color:black;font-size:12px;}A {color : black;}A.name {color : black;}HR {color : #525D76;}</style></head><body><h1>HTTP Status 500 – Internal Server Error</h1><hr class="line" /><p><b>Type</b> Exception Report</p><p><b>Message</b> java.lang.NoSuchMethodError: com.fasterxml.jackson.core.JsonStreamContext.&lt;init&gt;(II)V</p><p><b>Description</b> The server encountered an unexpected condition that prevented it from fulfilling the request.</p><p><b>Exception</b> <pre>org.jboss.resteasy.spi.UnhandledException: java.lang.NoSuchMethodError: com.fasterxml.jackson.core.JsonStreamContext.&lt;init&gt;(II)V
                             		org.jboss.resteasy.core.ExceptionHandler.handleApplicationException(ExceptionHandler.java:76)
                             		org.jboss.resteasy.core.ExceptionHandler.handleException(ExceptionHandler.java:212)
                             		org.jboss.resteasy.core.SynchronousDispatcher.writeException(SynchronousDispatcher.java:149)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$xnx7rCew(SynchronousDispatcher.java:372)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$xnx7rCew$accessor$9qp6jkVp(SynchronousDispatcher.java)
                             		org.jboss.resteasy.core.SynchronousDispatcher$auxiliary$CtgQat61.call(Unknown Source)
                             		software.amazon.disco.agent.web.resteasy.service.RestEasyHttpServiceActivityInterceptor.intercept(RestEasyHttpServiceActivityInterceptor.java:94)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke(SynchronousDispatcher.java)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$jXZCUqt8(SynchronousDispatcher.java:179)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$jXZCUqt8$accessor$NJ1uxcIY(SynchronousDispatcher.java)
                             		org.jboss.resteasy.core.SynchronousDispatcher$auxiliary$tlPmoTPi.call(Unknown Source)
                             		com.amazon.alphaone.agent.interception.arest.ArestServiceNameOverrideInterceptor$ArestServiceNameCollector.intercept(ArestServiceNameOverrideInterceptor.java:120)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke(SynchronousDispatcher.java)
                             		org.jboss.resteasy.plugins.server.servlet.ServletContainerDispatcher.service(ServletContainerDispatcher.java:220)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service(HttpServletDispatcher.java:56)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service$original$VG2IBvtq(HttpServletDispatcher.java:51)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service$original$VG2IBvtq$accessor$Faszi7ou(HttpServletDispatcher.java)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher$auxiliary$KUCEAqdn.call(Unknown Source)
                             		software.amazon.disco.agent.web.servlet.HttpServletServiceInterceptor.service(HttpServletServiceInterceptor.java:129)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service(HttpServletDispatcher.java)
                             		javax.servlet.http.HttpServlet.service(HttpServlet.java:727)
                             		com.amazon.arest.metrics.ARestQuerylogFilter.doFilter(ARestQuerylogFilter.java:58)
                             	</pre></p><p><b>Root Cause</b> <pre>java.lang.NoSuchMethodError: com.fasterxml.jackson.core.JsonStreamContext.&lt;init&gt;(II)V
                             		com.fasterxml.jackson.databind.util.TokenBufferReadContext.&lt;init&gt;(TokenBufferReadContext.java:59)
                             		com.fasterxml.jackson.databind.util.TokenBufferReadContext.createRootContext(TokenBufferReadContext.java:89)
                             		com.fasterxml.jackson.databind.util.TokenBuffer$Parser.&lt;init&gt;(TokenBuffer.java:1298)
                             		com.fasterxml.jackson.databind.util.TokenBuffer.asParser(TokenBuffer.java:276)
                             		com.fasterxml.jackson.databind.util.TokenBuffer.asParser(TokenBuffer.java:242)
                             		com.fasterxml.jackson.databind.ObjectMapper._convert(ObjectMapper.java:3732)
                             		com.fasterxml.jackson.databind.ObjectMapper.convertValue(ObjectMapper.java:3669)
                             		com.amazon.alexa.adcs.client.helper.ADCSClientHelper.getCapabilities(ADCSClientHelper.java:98)
                             		com.amazon.dee.device.remote.RemoteDevice.queryDeviceCapabilitiesFromADCS(RemoteDevice.java:929)
                             		com.amazon.dee.device.remote.RemoteDevice.queryDeviceCapabilities(RemoteDevice.java:905)
                             		com.amazon.dee.device.remote.RemoteDevice.buildDeviceCapabilityCacheIfEmpty(RemoteDevice.java:880)
                             		com.amazon.dee.device.remote.RemoteDevice.getDeviceCapabilitiesMap(RemoteDevice.java:850)
                             		com.amazon.dee.device.remote.RemoteDevice.getCapability(RemoteDevice.java:322)
                             		com.amazon.dee.device.remote.RemoteDevice.hasCapability(RemoteDevice.java:588)
                             		com.amazon.dee.device.remote.RemoteDevice.hasCapability(RemoteDevice.java:458)
                             		com.amazon.alexa.timers.renderer.util.DeviceCapabilitiesUtil.hasScreen(DeviceCapabilitiesUtil.java:62)
                             		com.amazon.alexa.timers.renderer.util.DeviceCapabilitiesUtil.canHandleListNotifications(DeviceCapabilitiesUtil.java:23)
                             		com.amazon.alexa.timers.renderer.util.LocalAppUtil.sendListNotifications(LocalAppUtil.java:47)
                             		com.amazon.alexa.timers.renderer.activity.RenderDeviceImpl.sendListNotifications(RenderDeviceImpl.java:34)
                             		com.amazon.alexatimersapiservice.util.DisplayComponent.sendListDirectiveToDeviceIfRequired(DisplayComponent.java:47)
                             		com.amazon.alexatimersapiservice.actions.CreateTimerAction.createTimer(CreateTimerAction.java:38)
                             		com.amazon.alexatimersapiservice.controllers.TimersController.createTimer(TimersController.java:105)
                             		sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                             		sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
                             		sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                             		java.lang.reflect.Method.invoke(Method.java:498)
                             		org.jboss.resteasy.core.MethodInjectorImpl.invoke(MethodInjectorImpl.java:137)
                             		org.jboss.resteasy.core.ResourceMethodInvoker.invokeOnTarget(ResourceMethodInvoker.java:296)
                             		org.jboss.resteasy.core.ResourceMethodInvoker.invoke(ResourceMethodInvoker.java:250)
                             		org.jboss.resteasy.core.ResourceMethodInvoker.invoke(ResourceMethodInvoker.java:237)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$xnx7rCew(SynchronousDispatcher.java:356)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$xnx7rCew$accessor$9qp6jkVp(SynchronousDispatcher.java)
                             		org.jboss.resteasy.core.SynchronousDispatcher$auxiliary$CtgQat61.call(Unknown Source)
                             		software.amazon.disco.agent.web.resteasy.service.RestEasyHttpServiceActivityInterceptor.intercept(RestEasyHttpServiceActivityInterceptor.java:94)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke(SynchronousDispatcher.java)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$jXZCUqt8(SynchronousDispatcher.java:179)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$jXZCUqt8$accessor$NJ1uxcIY(SynchronousDispatcher.java)
                             		org.jboss.resteasy.core.SynchronousDispatcher$auxiliary$tlPmoTPi.call(Unknown Source)
                             		com.amazon.alphaone.agent.interception.arest.ArestServiceNameOverrideInterceptor$ArestServiceNameCollector.intercept(ArestServiceNameOverrideInterceptor.java:120)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke(SynchronousDispatcher.java)
                             		org.jboss.resteasy.plugins.server.servlet.ServletContainerDispatcher.service(ServletContainerDispatcher.java:220)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service(HttpServletDispatcher.java:56)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service$original$VG2IBvtq(HttpServletDispatcher.java:51)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service$original$VG2IBvtq$accessor$Faszi7ou(HttpServletDispatcher.java)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher$auxiliary$KUCEAqdn.call(Unknown Source)
                             		software.amazon.disco.agent.web.servlet.HttpServletServiceInterceptor.service(HttpServletServiceInterceptor.java:129)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service(HttpServletDispatcher.java)
                             		javax.servlet.http.HttpServlet.service(HttpServlet.java:727)
                             		com.amazon.arest.metrics.ARestQuerylogFilter.doFilter(ARestQuerylogFilter.java:58)
                             	</pre></p><p><b>Note</b> The full stack trace of the root cause is available in the server logs.</p><hr class="line" /></body></html>
                             	Traceback (most recent call last):
                             	  File "/var/task/ask_sdk_core/serialize.py", line 165, in deserialize
                             	    payload = json.loads(payload)
                             	  File "/var/lang/lib/python3.8/json/__init__.py", line 357, in loads
                             	    return _default_decoder.decode(s)
                             	  File "/var/lang/lib/python3.8/json/decoder.py", line 337, in decode
                             	    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
                             	  File "/var/lang/lib/python3.8/json/decoder.py", line 355, in raw_decode
                             	    raise JSONDecodeError("Expecting value", s, err.value) from None
                             	json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
                             	
                             	During handling of the above exception, another exception occurred:
                             	
                             	Traceback (most recent call last):
                             	  File "/var/task/ask_sdk_runtime/dispatch.py", line 118, in dispatch
                             	    output = self.__dispatch_request(handler_input)  # type: Union[Output, None]
                             	  File "/var/task/ask_sdk_runtime/dispatch.py", line 182, in __dispatch_request
                             	    output = supported_handler_adapter.execute(
                             	  File "/var/task/ask_sdk_runtime/dispatch_components/request_components.py", line 437, in execute
                             	    return handler.handle(handler_input)
                             	  File "/var/task/lambda_function.py", line 567, in handle
                             	    timer_response = timer_service.create_timer(timer_request)
                             	  File "/var/task/ask_sdk_model/services/timer_management/timer_management_service_client.py", line 502, in create_timer
                             	    api_response = self.invoke(
                             	  File "/var/task/ask_sdk_model/services/base_service_client.py", line 148, in invoke
                             	    exception_body = self._serializer.deserialize(
                             	  File "/var/task/ask_sdk_core/serialize.py", line 167, in deserialize
                             	    raise SerializationException(
                             	ask_sdk_core.exceptions.SerializationException: Couldn't parse response body: <!doctype html><html lang="en"><head><title>HTTP Status 500 – Internal Server Error</title><style type="text/css">H1 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:22px;} H2 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:16px;} H3 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:14px;} BODY {font-family:Tahoma,Arial,sans-serif;color:black;background-color:white;} B {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;} P {font-family:Tahoma,Arial,sans-serif;background:white;color:black;font-size:12px;}A {color : black;}A.name {color : black;}HR {color : #525D76;}</style></head><body><h1>HTTP Status 500 – Internal Server Error</h1><hr class="line" /><p><b>Type</b> Exception Report</p><p><b>Message</b> java.lang.NoSuchMethodError: com.fasterxml.jackson.core.JsonStreamContext.&lt;init&gt;(II)V</p><p><b>Description</b> The server encountered an unexpected condition that prevented it from fulfilling the request.</p><p><b>Exception</b> <pre>org.jboss.resteasy.spi.UnhandledException: java.lang.NoSuchMethodError: com.fasterxml.jackson.core.JsonStreamContext.&lt;init&gt;(II)V
                             		org.jboss.resteasy.core.ExceptionHandler.handleApplicationException(ExceptionHandler.java:76)
                             		org.jboss.resteasy.core.ExceptionHandler.handleException(ExceptionHandler.java:212)
                             		org.jboss.resteasy.core.SynchronousDispatcher.writeException(SynchronousDispatcher.java:149)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$xnx7rCew(SynchronousDispatcher.java:372)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$xnx7rCew$accessor$9qp6jkVp(SynchronousDispatcher.java)
                             		org.jboss.resteasy.core.SynchronousDispatcher$auxiliary$CtgQat61.call(Unknown Source)
                             		software.amazon.disco.agent.web.resteasy.service.RestEasyHttpServiceActivityInterceptor.intercept(RestEasyHttpServiceActivityInterceptor.java:94)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke(SynchronousDispatcher.java)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$jXZCUqt8(SynchronousDispatcher.java:179)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$jXZCUqt8$accessor$NJ1uxcIY(SynchronousDispatcher.java)
                             		org.jboss.resteasy.core.SynchronousDispatcher$auxiliary$tlPmoTPi.call(Unknown Source)
                             		com.amazon.alphaone.agent.interception.arest.ArestServiceNameOverrideInterceptor$ArestServiceNameCollector.intercept(ArestServiceNameOverrideInterceptor.java:120)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke(SynchronousDispatcher.java)
                             		org.jboss.resteasy.plugins.server.servlet.ServletContainerDispatcher.service(ServletContainerDispatcher.java:220)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service(HttpServletDispatcher.java:56)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service$original$VG2IBvtq(HttpServletDispatcher.java:51)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service$original$VG2IBvtq$accessor$Faszi7ou(HttpServletDispatcher.java)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher$auxiliary$KUCEAqdn.call(Unknown Source)
                             		software.amazon.disco.agent.web.servlet.HttpServletServiceInterceptor.service(HttpServletServiceInterceptor.java:129)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service(HttpServletDispatcher.java)
                             		javax.servlet.http.HttpServlet.service(HttpServlet.java:727)
                             		com.amazon.arest.metrics.ARestQuerylogFilter.doFilter(ARestQuerylogFilter.java:58)
                             	</pre></p><p><b>Root Cause</b> <pre>java.lang.NoSuchMethodError: com.fasterxml.jackson.core.JsonStreamContext.&lt;init&gt;(II)V
                             		com.fasterxml.jackson.databind.util.TokenBufferReadContext.&lt;init&gt;(TokenBufferReadContext.java:59)
                             		com.fasterxml.jackson.databind.util.TokenBufferReadContext.createRootContext(TokenBufferReadContext.java:89)
                             		com.fasterxml.jackson.databind.util.TokenBuffer$Parser.&lt;init&gt;(TokenBuffer.java:1298)
                             		com.fasterxml.jackson.databind.util.TokenBuffer.asParser(TokenBuffer.java:276)
                             		com.fasterxml.jackson.databind.util.TokenBuffer.asParser(TokenBuffer.java:242)
                             		com.fasterxml.jackson.databind.ObjectMapper._convert(ObjectMapper.java:3732)
                             		com.fasterxml.jackson.databind.ObjectMapper.convertValue(ObjectMapper.java:3669)
                             		com.amazon.alexa.adcs.client.helper.ADCSClientHelper.getCapabilities(ADCSClientHelper.java:98)
                             		com.amazon.dee.device.remote.RemoteDevice.queryDeviceCapabilitiesFromADCS(RemoteDevice.java:929)
                             		com.amazon.dee.device.remote.RemoteDevice.queryDeviceCapabilities(RemoteDevice.java:905)
                             		com.amazon.dee.device.remote.RemoteDevice.buildDeviceCapabilityCacheIfEmpty(RemoteDevice.java:880)
                             		com.amazon.dee.device.remote.RemoteDevice.getDeviceCapabilitiesMap(RemoteDevice.java:850)
                             		com.amazon.dee.device.remote.RemoteDevice.getCapability(RemoteDevice.java:322)
                             		com.amazon.dee.device.remote.RemoteDevice.hasCapability(RemoteDevice.java:588)
                             		com.amazon.dee.device.remote.RemoteDevice.hasCapability(RemoteDevice.java:458)
                             		com.amazon.alexa.timers.renderer.util.DeviceCapabilitiesUtil.hasScreen(DeviceCapabilitiesUtil.java:62)
                             		com.amazon.alexa.timers.renderer.util.DeviceCapabilitiesUtil.canHandleListNotifications(DeviceCapabilitiesUtil.java:23)
                             		com.amazon.alexa.timers.renderer.util.LocalAppUtil.sendListNotifications(LocalAppUtil.java:47)
                             		com.amazon.alexa.timers.renderer.activity.RenderDeviceImpl.sendListNotifications(RenderDeviceImpl.java:34)
                             		com.amazon.alexatimersapiservice.util.DisplayComponent.sendListDirectiveToDeviceIfRequired(DisplayComponent.java:47)
                             		com.amazon.alexatimersapiservice.actions.CreateTimerAction.createTimer(CreateTimerAction.java:38)
                             		com.amazon.alexatimersapiservice.controllers.TimersController.createTimer(TimersController.java:105)
                             		sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                             		sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
                             		sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                             		java.lang.reflect.Method.invoke(Method.java:498)
                             		org.jboss.resteasy.core.MethodInjectorImpl.invoke(MethodInjectorImpl.java:137)
                             		org.jboss.resteasy.core.ResourceMethodInvoker.invokeOnTarget(ResourceMethodInvoker.java:296)
                             		org.jboss.resteasy.core.ResourceMethodInvoker.invoke(ResourceMethodInvoker.java:250)
                             		org.jboss.resteasy.core.ResourceMethodInvoker.invoke(ResourceMethodInvoker.java:237)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$xnx7rCew(SynchronousDispatcher.java:356)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$xnx7rCew$accessor$9qp6jkVp(SynchronousDispatcher.java)
                             		org.jboss.resteasy.core.SynchronousDispatcher$auxiliary$CtgQat61.call(Unknown Source)
                             		software.amazon.disco.agent.web.resteasy.service.RestEasyHttpServiceActivityInterceptor.intercept(RestEasyHttpServiceActivityInterceptor.java:94)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke(SynchronousDispatcher.java)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$jXZCUqt8(SynchronousDispatcher.java:179)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke$original$jXZCUqt8$accessor$NJ1uxcIY(SynchronousDispatcher.java)
                             		org.jboss.resteasy.core.SynchronousDispatcher$auxiliary$tlPmoTPi.call(Unknown Source)
                             		com.amazon.alphaone.agent.interception.arest.ArestServiceNameOverrideInterceptor$ArestServiceNameCollector.intercept(ArestServiceNameOverrideInterceptor.java:120)
                             		org.jboss.resteasy.core.SynchronousDispatcher.invoke(SynchronousDispatcher.java)
                             		org.jboss.resteasy.plugins.server.servlet.ServletContainerDispatcher.service(ServletContainerDispatcher.java:220)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service(HttpServletDispatcher.java:56)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service$original$VG2IBvtq(HttpServletDispatcher.java:51)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service$original$VG2IBvtq$accessor$Faszi7ou(HttpServletDispatcher.java)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher$auxiliary$KUCEAqdn.call(Unknown Source)
                             		software.amazon.disco.agent.web.servlet.HttpServletServiceInterceptor.service(HttpServletServiceInterceptor.java:129)
                             		org.jboss.resteasy.plugins.server.servlet.HttpServletDispatcher.service(HttpServletDispatcher.java)
                             		javax.servlet.http.HttpServlet.service(HttpServlet.java:727)
                             		com.amazon.arest.metrics.ARestQuerylogFilter.doFilter(ARestQuerylogFilter.java:58)
                             	</pre></p><p><b>Note</b> The full stack trace of the root cause is available in the server logs.</p><hr class="line" /></body></html>
2020-10-06T08:42:38.271-04:00	END RequestId: 50f7b68d-55d1-4bbd-a25b-e3fd8f32a238
2020-10-06T08:42:38.271-04:00	REPORT RequestId: 50f7b68d-55d1-4bbd-a25b-e3fd8f32a238	Duration: 879.26 ms	Billed Duration: 900 ms	Memory Size: 128 MB	Max Memory Used: 113 MB	
'''
