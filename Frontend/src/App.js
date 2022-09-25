import React, {useState} from 'react';
import LoginForm from './components/LoginForm';
function App(){
  const adminUser = {
    name: "admin",
    password:"admin123"
  }
  const [user, setUser] = useState({name:""});
  const [error, setError] = useState("");
  const Login = details => {
    console.log(details);
    if(details.name===adminUser.name && details.password===adminUser.password){
    console.log("Logged in");
    setUser({
      name: details.name,
      password: details.password
    });
  }
    else {
    console.log("Details do not match!");
    setError("Details do not match!");
    }
  }
  const Logout = () => {
    setUser({name:""});
  }
  return (
    <div className='App'>
      {(user.name !== "") ? (
        <div className='Welcome'>
          <h2> Welcome, <span>{user.name}</span></h2>
          <button onClick={Logout}>Logout</button>
        </div>
      ) : (
        <LoginForm Login={Login} error={error}/>
      )}
    </div>

  );
}
export default App;