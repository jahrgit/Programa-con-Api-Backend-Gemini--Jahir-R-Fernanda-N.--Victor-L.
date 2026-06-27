
import {Fragment,memo,useCallback,useContext,useEffect} from "react"
import {ReflexEvent,applyEventActions,isTrue} from "$/utils/state"
import {EventLoopContext} from "$/utils/context"
import {jsx} from "@emotion/react"






export const Button_button_e9a9c9c49b553224398d78334c37d45a = memo(({children}) => {
    const [addEvents, connectErrors] = useContext(EventLoopContext);
const on_click_394880e555cb8a7cf2cd0cfec57df0fe = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.api_programas___api_programas____state.limpiar", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])



    return(
        jsx("button",{className:"btn-borrar",onClick:on_click_394880e555cb8a7cf2cd0cfec57df0fe},children)
    )
});
