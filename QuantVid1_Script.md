"I think I can safely say that nobody understands quantum mechanics" — _Richard P. Feynman_
$$-13.6eV.$$
If you are a science student, I am sure you somewhat familiar with this number. If you may recall, it might have appeared in your high school chemistry class, or perhaps in a introductory physics class you first heard about the atomic model; Perhaps it is out of curiosity that you asked your teacher "what is the energy of an electron" and what you get is this rather mysterious number. Or perhaps you have seen the energy level equation,
$$
\Delta E = -13.6eV \left( \frac{1}{n^2_{f}}-\frac{1}{n_{i}^2} \right)
$$
in you waves mechanic class, which explains the transition energy for a electron in a hydrogen atom.

Now this equation looks clean, but if you are a little more involved in the physics community, you might know that getting this equation might not be the easiest task. Well, to be precise, to obtain this equation we need to "solve the Schrödinger equation for hydrogen atom". 

If you are confused, that is ok. Physics college students takes years of class after high school to prep for quantum mechanics. I find the problem hard even after all these course, it was long, several pages of derivation with some rather tedious calculations.

However, I do not think this is impossible to simplify it to a level that can be easily understood by people with little scientific background; At least in a more than hand wavy but far from rigorous way. You just need to know some very simple physics, some basic calculus and probability, and do a few algebraic manipulation tricks. And if you are a physics student looking to review some quantum mechanics, I hope this video also help you as well.

This will be a multi part video series that start from the big picture of quantum mechanics, and goes into finer details into by solving actual well known quantum mechanic problem.

In this video, I will give an overview of some most important concept of quantum mechanics by comparing it directly to its classical mechanics counterpart which you might be familiar with. This video is more of a How video, explaining how quantum mechanics differ from classical physics. By the end of this video, I am hoping that you would be familiar with some conceptual quantum quirkiness and get ready to tackle Schrödinger equation in the following video.

# Quantum State and Wave function
## Classical Physics
Before we begin QM, I want you to think about something rudimental, something too simple that might often been overlooked. I am asking how might a physicist describe some every day object like an apple?
 
 Well, there are essentially three important steps
1. We will first assign properties to the object, for example, an apple might be classified by where it is located at, which is its position and where is it moving, its momentum. 
2. We need to get some coordinate system, like for example if we are interested in its position, we might use two basis vectors to assign a 2D cartesian coordinate system. Maybe another momentum coordinate system telling us where it is going. Setting up the coordinate system allow us to represent the property we are interest in through some mathematical way, like $\text{PositionRep(Apple)}=(x,y,z)$, a set of numbers. 
3. We make measurements. For example, we say $\text{Position(Apple)}=(4,2)$ we meant the apple is located four units along the  $x$ axis $x\to 4$, and two units along the $y$ axis $y\to2$, respect to the origin. Here we simply need to just read off the coordinate system.
I have to point out the subtlety between position representation and position we get after measuring a value. You might think it is a bit overcomplicating it, and yes, that is true. In classical mechanics, we do not generally make this distinction, but as you will see later, quantum mechanics highlight a difference here.

Now begin exploring, I want you to imagine two objects, a regular apple like the one I was just describing, and a quantum apple, which I will describe in a quantum manner using the same three steps; and just for the sake of simplicity, I am going to reduce the position and momentum dimension to $1$. 
## Step 1: Representing Quantum Object
In the quantum world, quantum objects, like our quantum apple. are governed by what is called a quantum state, we generally use angled bracket called a ket with psi in it
$$\ket{\psi}$$
to denote it. A state sort of equivalent to the object itself. We have properties like position, momentum, energies, etc. all contained internally within the state. And thats it! Simple as that!
### What are these quantities?
But I want to mention something different here. When we assign property in QM, we are not guaranteed they can take up any value we like. There are two types, in particular
1. First, there have properties in nature that only discrete value (finite or infinite) are allowed. For example, spin, which will not be the focus here, and orbital angular momentum.
I want to emphasize When I talk about properties that are discrete, I really meant it. Nature is very biased, and there are certain values nature that is simply not allowed. For example, we can never have a angular momentum value of $3.32\hbar$ at any situation. Angular momentum takes on integer multiples of $\hbar$. I also what to highlight the number allowed of angular momentum is bounded by $m$ called the magnetic quantum number, some property of the object. This can be counterintuitive when we try to apply quantum mechanics on macroscopic objects, but keep in mind our standard unit of angular momentum $\hbar$ is a very small number, which means to get angular momentum value that is sensible in real life the upper limit of angular moment $m$  needs to be very large. So at large we approximately see they are continueous.
2. Properties allowing to take up any value, for example position and momentum. They are a lot less interesting, similar to that of classical mechanics.
Here I want to mention a really important terminology, and I want you to memorize it. We call the allowed value of some property the eigenvalue of that property.
### Take a break
_A more formal discussion on of the limitation of properties involves recognizing that every physical property has its representation as a subspace of some extended Hilbert space, with either finite or uncountably infinite set of basis vector called eigenvectors associated with the eigenvalue, with each eigenvalue representing some physically measurable value. Of course, this is worthy of half semester of material in a rigorous QM class, though we will briefly talk about eigenvectors and eigenvalues later, I wont get into too much of this formalism._

## Step 2: Setup coordinate system
Now that we have the state $\ket{\psi}$ representing our quantum apple. Second step is to set up a coordinate. In quantum mechanics we can mathematically represent a quantum state living in some coordinate system, by sticking this leftward facing angle bracket known as a bra 
$$\bra{x}$$
to it.
$$
\braket{ x |\psi  }=\psi(x)
$$
In this notation, you should read this equation as, given some particle $\ket{\psi}$, in our case, the quantum apple, what is the representation of that state in the position coordinate system $\bra{x}$. If we are instead interested in setting up a momentum coordinate system, we can write the momentum symbol instead $\braket{ p_{x} |\psi  }$, but I will stick with $x$ for the analysis, and you can imagine the same thing done on momentum later because the logics are the same. Now look at the right hand side... $\psi(x)$ this is where it gets interesting...

Think about a single dimension in classical system. When we talk about the location of an apple on the x axis, ultimately our goal is to describe the position $x$ with some number. So we can write the position representation of the apple equal to $x$, its measured position. ($\text{PositionRep(Apple)}=x=\text{Position(Apple)}$). The left hand side of both highlighted equations ($\braket{ x |\psi  }=\psi(x)$, and $\text{PositionRep(Apple)}=x$) physically represent the same clause, is just the quantum way has a fancy notation. Now on the right hand side, it seems like quantum is suggesting the representation of our quantum apple in x position coordinate system is so called a wave function

This is definitely uncharted territory, because, seriously, it really does not make sense to say, our quantum apple is located at, some complicated function ($x \overset{\text{wtf???}}{\to}\left(  \frac{m\omega}{\pi\hbar} \right)^{1/4} \exp\left( -\frac{m\omega x^2}{2\hbar} \right)=\psi(x)$). And I am hoping I have motivated you enough to believe that the position coordinate system does not necessarily tell us about the precise position. The takeaway is, in QM we make the distinction between the measured physical quantity and the coordinate representation of that quantity. And in general, they are not equal. 

The thing is, when we think of classical mechanic, representing an object in a coordinate and making a measurement base on it is essentially the same, and that is why we generally do not consider them as separate steps in CM. What I am saying is if we already know the apple is at position, the only thing that can change it is some equation of motion ($\vec{F}=m \vec{a}=\frac{d\vec{p}}{dt}$) that depends on time. In quantum mechanics, this is not the full story. Yes we have a equation of motion called the Schrödinger equation that changes the state and hence position over time. But there is also some sort of inherent randomness when measuring. The reason we have this phenomenon is because certain quantum properties can be  intertwined, like position and momentum. For example, if we are given position coordinate system and a momentum coordinate system, measuring position will actually change the momentum and vice versa. You might have heard about Heisenberg uncertainty principle; and there are actually a set of them, but the most famous one is this on the screen.
$$
\Delta x\Delta p_{x} \ge \frac{\hbar}{2}
$$You may need to take some time to interpret equation. The triangle here is the statical variance of repeated measurement taking account of the randomness. It is associated with the range where we are 68% sure about the where measurement is going to land. The takeaway of this equation is that __for two incompatible property of an quantum object, maximum certainty in a single quantity means maximum uncertainty in the other__. So here, if I know the exact position of our quantum apple, then I will have no idea what its momentum is. To re-emphasize what we have learned here, quantum object measurement are not always the same, and source of randomness comes from __incompatibility__ of properties captured by this principle. And that is why we should not really assign exact quantity to properties.

### Take a Break
Previously we have compared Newton's Law with Schrödinger's equation, but this is kind of hand wavy. After all, newton's law are about positions and momentum evolution with time, while Schrödinger equation is about state energy evolution with time (and possibly position if in that representation). A more appropriate comparison is to Hamiltonian mechanics, which is equivalent to newtonian mechanics but formulated in a way that relates position and momentum with energy. In this sense, we can say Schrödinger's equation is like (use $q$ for position),
$$
\frac{ \partial p }{ \partial t } =-\frac{ \partial H }{ \partial q }, \, \frac{ \partial q }{ \partial t } =\frac{ \partial H }{ \partial p } 
$$
## Step 3: Measurements
Now the last step is to talk about how to precisely we can make a measurement. Since wave functions are coordinate representation of our quantum apple, it should at least capture the probabilistic/uncertain nature of measurements that we were talking about. How this work is proposed by Max Born: The wave function in some coordinate system, when squared is a probability density function of measuring the associated property of the coordinate system. And when you integrate a probability density function, you expect the area under the curve gives us the probability. 
$$
\int_{a}^b|\psi(x)|^2dx=\text{Probability of getting measuremt of } x \text{ in range }[a,b] 
$$
And of course, there are nothing preventing us to do the same for momentum.
$$
\int_{a}^b|\psi(p_{x})|^2dp_{x}=\text{Probability of getting measuremt of } p \text{ in range }[a,b] 
$$
I do want to make a few remarks here. 
1. Because the above represents a probability, it is most natural to require $$
\int_{-\infty}^\infty|\psi(x)|^2dx=1
$$sum of all probability across all position is $1$. When dealing with equations in quantum mechanics, this property is not always automatically satisfied. To enforcing this is called normalizing the wave function. 
2. $\psi(x)$ most of time is generally a complex function. That means this function might contain this weird number $\sqrt{ -1}=i$. It can be weird to interpret it at first, because $i$ is not a physical. But think again, the wave function does not need to be physical. It is just a mathematical tool to describe quantum effects, and as long as measurements of wave functions are physical, then our tool wont cause any trouble.

Now we know wave function and probability of measurement, what about measurement it self? Well, we do so by by placing what we called _operator_ next to the state or wave function. These are the little hats on properties.
$$
\hat{x}\ket{\psi}  \text{ or }\hat{x}\psi(x) \text{ or }\hat{x}\psi(p_{x})
$$
Note that we can measure directly on quantum state. So coordinate is not absolutely necessary, but it is certainly very nice to have, because thats how we can actually draw values from the probability distribution. Also note that we are allowed to extract the position of an object represented the momentum coordinate system. And that is totally fine. Wavefunction is just a representation of the state it self, which contains all property we are interested in. We just need to convert the operator to the appropriate coordinate system
$$
\hat{x}=x \leftarrow \text{Position Coordinate};\; \hat{x}=i\hbar \frac{ \partial }{ \partial p } \leftarrow \text{Momentum Coordinate}
$$
We can of course, do all kinds of probability measurement using them. But these will not be our focus today.

I want to mention, a very subtle but useful way to think about the probabilistic nature of value here. Since eigenvalues represents all possible outcome of a measurement, we can imagine a pool of quantum states of some property like position, and for each of these state we demand that when measured, it will guarantee, with 100% certainty, yield the same eigenvalue every time. These are called eigenstates which represent using a ket and put the eigenvalue inside it.
$$
\ket{x}=\{ \ket{1} ,\ket{2} ,\ket{0.21},\ket{1/3},   \dots\} _{\leftarrow \text{ actuelly uncountable but you get the point}}
$$
As a side note I want to briefly mention that we can indeed have eigenstates corresponds to multiple physical properties as long as the properties are compatible to each other, this of course cannot happen if the properties that are incompatible, because in that cause it would break the uncertainty principle. This is a very complicated topic on its own, so I will not discuss details here.
$$
\ket{x,???}=\{ \ket{1,???_{1}} ,\ket{2,???_{2}} ,\ket{0.21,???_{3}},\ket{1/3, ???_{4}},   \dots\} _{\leftarrow \text{ actuelly uncountable but you get the point}}
$$
You might have noticed mathematically when applying the operator on a specific position eigenstate we do not merely get the position, but rather the position multiplied by the state itself. These equations are called eigenvalue equation, and it is structured in this way to represent a ground truth about measuring these special eigenstates. 
$$
\begin{align}
 & \hat{x}\ket{x_{0}}=x_{0}\ket{x_{0}}   & \implies &  \text{ e.g. }\hat{x}\ket{5} = 5\ket{5} \\  & \text{In position coordinate:} &  \\

 & \hat{x}\psi(x)=x_{0} \psi(x)  & \implies &  \psi(x)=\delta(x-x_{0})
\end{align}
$$
Depending on the property, eigenvalue equation can matrix or differential equation. This is particularly useful, because say if we have some unknown property, then we simply have to setup one of these equation and solve for it to get the eigenvalues, eigenstates or eigen-wave function. In other words, it is always possible to obtain eigenvalues and its corresponding states given some quantity, at the very least numerically. 

Well measurements on eigenstates is kind of straight forward because they are non probabilistic, for general object it might take on any allowed value with some probabilistic weight associated. When we make an measurement we should really think about sampling from our the pool of eigenstates. Physicist are kinda troubled to interpret this result, because probability means that we really cannot assign eigenstates to an object. Which means our quantum apple cannot be in one position. Well, disappointingly physicists cannot really agree on a physical interpretation of this. The most popular one, which is the one generally taught in textbook, is the Copenhagen interpretation. In popular media this interpretation is most often associated with Schrodinger's cat. It says that objet, our quantum apple, is in a superposition of all eigenstates, so it exist in all states, until a measurement will collapse the object into a single eigenstate. Notice that after the measurement, the object now __becomes__ eigenstates, and now repeated measurement will give same the respected eigenvalue. The part where our original probabilistic state turning into a definite value state after measurement should make philosophical sense, because other wise there would be no meaning of measurement. One last thing, since have measured, and known the exact position now, don't forget about the Heisenberg uncertainty principle: knowing the position will means maximum uncertainty in momentum.

### Take a break
More emphasis on $\psi$ possibly involve $i$: Having complex number involved is very fundamental to quantum mechanics, but is it really necessary? In linear algebra we can represent complex number as a 2x2 real matrix:
$$
z = a + bi, \, z \longleftrightarrow
\begin{pmatrix}
a & -b \\
b & a
\end{pmatrix}
$$
Theoretically we should be able to formulate QM using some matrix algebra, but it become much much complicated. we can think about complex number as some handy tool to simplify the calculation. It effectively avoiding us getting into the algebraic mess of some higher dimensional real Hilbert space.
### In person closure
Hi, I am Yichen. Thank you for watching till this part of the video. We have really seen a lot now: We discussed the three steps physicist use to describe an object in classical mechanics, that is representing the object, assigning coordinate system and making measurement, and we have seen now how they are can be very different in quantum mechanics. Like we can only have certain allowed value called eigenvalue. We also talked about properties can be interacting with each other through Heisenberg uncertainty principle, and we have also seen the wavefunction as probability distribution capturing the uncertainty in measurement. Lastly we discussed about the eigenstates and the Copenhagen interpretation of quantum mechanics. The next video will be more of an math/application one, we will be introducing the Schrödinger equation and perhaps go thought the algebraic process of solving the hydrogen atom that leads to the energy separation equation we have seen in the beginning of this video. Making these video takes me a long time, so if you enjoyed this video please consider subscribing to the channel and press the like button. Thanks for sticking around, peace out, bye!

# Misc
Simple physics
$$
\begin{gather}
\vec{F} =m\vec{a}=\frac{d \vec{p}}{dt} \text{ (Newton's Law)} \\
T =\frac{1}{2}mv^2=\frac{p^2}{2m} \text{ (Kinetic Energy)} \\
H=T+V \text{ (Total Energy)}
\end{gather}
$$
Basic calculus
$$
\begin{gather}
\frac{ \partial  }{ \partial t } \text{ (Derivatives)}  \\
\int \text{ (Integrals)} \\
\delta(x) \text{ (Dirac Delta Function)}  \\
PDF(x) \text{ (Probability Density Function)}
\end{gather}
$$
Basic Linear Algebra
$$
\begin{gather}
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix} \text{ (Matrix and Vectors)} \\
A\vec{x}=\lambda \vec{x} \text{ (Eigenvalue Equation)} \\
V \text{ (Vector Space)}
\end{gather}
$$