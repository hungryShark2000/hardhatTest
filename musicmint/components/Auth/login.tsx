import React, { useContext, useEffect, useState } from 'react';
import AuthContext from '../../src/context/auth';
import styles from '../../styles/marketplace.module.css';
import Wallet from '../../components/Auth/connectWallet'

const Login = (props) => {
    const { loginUser } = useContext(AuthContext);
    let [email, setEmail] = useState<any>(null)
    let [password, setPassword] = useState<any>(null)

    useEffect(() => {
        function handleKeyDown(event) {
          if (event.key === "Enter") {
            console.log(email);
            console.log(password);

            loginUser(email, password);
          }
        }

        window.addEventListener("keydown", handleKeyDown);
        return () => {
          window.removeEventListener("keydown", handleKeyDown);
        };
      }, [email, password]);

    return (
        <div className={styles.container}>
            <div className={styles.label}>MusicMint</div>
            <div>
                <div>Connect Wallet:</div>
                <Wallet web3Handler={props.web3Handler} account={props.account}></Wallet>
            </div>
            <div className={styles.header}>MusicMint</div>
                <div className={styles.formGroup}>
                    <input type="email" id="email" name="email" className={styles.input} onChange={(e) => setEmail(e.target.value)} placeholder="Enter your E-mail"/>
                </div>
                <div className={styles.formGroup}>
                    <input type="password" id="password" name="password" className={styles.input} onChange={(e) => setPassword(e.target.value)}  placeholder="Enter your password"/>
                </div>
                <div className={styles.formGroup}>
                    <div className={styles.button} onClick={() => loginUser(email, password)}>Log in</div>
                </div>
                <div className={styles.noCredentials}>
                    <div>Forgot password?</div>
                    <div onClick={props.switchTab}>Register</div>
                </div>
        </div>
    );
};

export default Login;