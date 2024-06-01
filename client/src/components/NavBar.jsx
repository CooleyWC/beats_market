import React from 'react';
import {NavLink, Link, Outlet} from 'react-router-dom'

function NavBar() {
    return (
        <>
        <nav>
            <NavLink to='/'>Home</NavLink>
        </nav>
        <main>
            <Outlet />
        </main>
        </>
    );
}

export default NavBar;