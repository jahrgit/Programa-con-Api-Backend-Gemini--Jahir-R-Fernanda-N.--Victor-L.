
import {Fragment,memo,useCallback,useContext,useEffect} from "react"
import {ReflexEvent,applyEventActions,isTrue} from "$/utils/state"
import {Button as RadixThemesButton} from "@radix-ui/themes"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {jsx} from "@emotion/react"






export const Button_button_a3e858cd378cfb4df423c4ea29a63c6e = memo(({children}) => {
    const [addEvents, connectErrors] = useContext(EventLoopContext);
const on_click_32da347507ae716c9f3d89fb4ed65648 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.api_programas___api_programas____state.enviar_pregunta", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])
const reflex___state____state__api_programas___api_programas____state = useContext(StateContexts.reflex___state____state__api_programas___api_programas____state)



    return(
        jsx(RadixThemesButton,{disabled:reflex___state____state__api_programas___api_programas____state.cargando_rx_state_,onClick:on_click_32da347507ae716c9f3d89fb4ed65648},children)
    )
});
