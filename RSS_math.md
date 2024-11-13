# RSS ANOVA Proof

Let $X = [X_0, X_1] \in \mathbb{R}^{n \times p}$ for $X_0 \in \mathbb{R}^{n \times p_0}$ and $X_1 \in \mathbb{R}^{n \times p_1}$ for $p=p_0+p_1$.

Let's apply the Gram–Schmidt Procedure to the columns of $X$. We assume that $X$ has linearly independant columns $x_0...x_p$.

$$
x_0 \ ... \ x_{p_0} ... \ x_p  \xrightarrow{\text{Gram–Schmidt}} u_0 \ ... \ u_{p_0} ... \ u_p
$$

Let $U_0 = \text{span}(u_0,... \ u_{p_0})$ and 
$U_1 = \text{span}(u_{p_0+1},... \ u_{p_0+p_1})$.

Then, by construction, $U_0 \oplus U_1 = \text{span}(X)$ and $U_0 = span(X_0)$ with $U_0$ orthogonal to $U_1$.

By definition of the least sqaures soution,
$X_0 \hat{\beta_0}=P_{U_0}\ y$ and 
$X \hat{\beta} = P_{U_0 \oplus U_1}\ y$.

$$
\begin{align*}
    &X_0 \hat{\beta_0} &&= P_{U_0}\ y
    \\
    &X \hat{\beta} &&= P_{U_0 \oplus U_1}\ y

\end{align*}
$$

The observed residuals are simply $y$ minus their projected component in each model's column space. 

$$
\begin{align*}
    \hat{\epsilon} &= y - P_{U_0 \oplus U_1}\ y
    \\
    \hat{\epsilon_0} &= y - P_{U_0}\ y
\end{align*}
$$

We then see that 

$$
\begin{equation}
    \hat{\epsilon_0} - \hat{\epsilon} = 
    P_{U_0 \oplus U_1}\ y - P_{U_0}\ y = P_{U_1}\ y
\end{equation}

$$ 

The last equals is a result of properties of orthogonal projection: $\forall v \in V=\mathbb{R^n}$ it holds that,

$$
P_{U_0 \oplus U_1}v = \underbrace{
    \langle v, u_0 \rangle u_0 + ... + 
    \langle v, u_{p_0} \rangle u_{p_0}
    }_{P_{U_0}v}
    +
    \underbrace{
        \langle v, u_{p_0+1} \rangle u_{p_0+1} + ... +
        \langle v, u_{p_0+p_1} \rangle u_{p_0+p_1}

    }_{P_{U_1}v}

$$

We then see that the true error term $\epsilon$ that is standard normal in $\mathbb{R}^n$. Projecting into $U_1$ gives

$$
P_{U_1}\ \epsilon = P_{U_1}\ y - P_{U_1}\ X \beta_0 = P_{U_1}\ y
$$

since $X \beta_0 \in U_0$. Therefore it holds that 

$$
\hat{\epsilon_0} - \hat{\epsilon} = P_{U_1}\ \epsilon
$$