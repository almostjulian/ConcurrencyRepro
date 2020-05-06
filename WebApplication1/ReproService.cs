using ServiceStack;


namespace WebApplication1
{
    public class User
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string MiddleName { get; set; }
        public string Initials { get; set; }
        public string DisplayName { get; set; }
        public string UserName { get; set; }
        public string EmployeeId { get; set; }
        public string EmployeeType { get; set; }
        public string FwGroup { get; set; }
        public string Email { get; set; }
    }

    [Route("/users/{UserName}", "GET", Summary = "Lists a single user")]
    public class GetUser : IReturn<User>
    {
        public string UserName { get; set; }
    }
    public class ReproService : Service
    {
        [CacheResponse(Duration = 43200, MaxAge = 21600)]
        public User Any(GetUser request)
        {
            return GetUser(request.UserName);
        }
        public static User GetUser(string userName)
        {
            string json =
                $"{{\"firstName\":\"{userName}\",\"lastName\":\"{userName}\",\"displayName\":\"{userName}\",\"userName\":\"{userName}\",\"employeeId\":\"9999\",\"employeeType\":\"E\",\"fwGroup\":\"Test\",\"email\":\"{userName}@foo.com\"}}";

            return json.FromJson<User>();
        }

    }
}