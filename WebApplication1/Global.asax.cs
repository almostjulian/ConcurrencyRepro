using Funq;
using ServiceStack;
using ServiceStack.DataAnnotations;
using ServiceStack.Text;
using System;
using System.Collections.Generic;

namespace WebApplication1
{
    public class AppHost : AppHostBase
    {
        public AppHost() : base("Concurrency Test API", typeof(AppHost).Assembly)
        {            
        }

        public override void Configure(Container container)
        {
            Env.StrictMode = true;
            JsConfig.Init(new ServiceStack.Text.Config
            {
                DateHandler = DateHandler.ISO8601,
                SkipDateTimeConversion = true,
                TextCase = TextCase.CamelCase,
                ExcludeTypeInfo = true
            });

            SetConfig(new HostConfig
            {
                MapExceptionToStatusCode = { { typeof(KeyNotFoundException), 404 } },
                Return204NoContentForEmptyResponse = true
            }
            );
        }
    }

    public class Global : System.Web.HttpApplication
    {
        protected void Application_Start(object sender, EventArgs e)
        {
            new AppHost().Init();
        }
       
    }
}