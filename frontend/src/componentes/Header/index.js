import Logo from "../Logo"
import IconesHeader from "../IconesHeader"
import OpcoesHeader from "../OpcoesHeader"
import styled from "styled-components"
import { Link } from "react-router-dom"


const HeaderContainer = styled.header`
  justify-content: center;
  background-color: #FFF;
  display: flex;
`


function Header() {
  return (
    <HeaderContainer>
      <Link to="/">
        <Logo />
      </Link>
      <OpcoesHeader />
      <IconesHeader />
    </HeaderContainer>
  )
}

export default Header;
